"""Basamak tanıtım kaydını Gemini Pro'ya gönderir ve raporu kaydeder.

1. Kullanılabilir modellerden en yeni "pro" modeli seçer.
2. Videoyu Files API ile yükler, işlenmesini bekler.
3. Videoyu (saniyede 5 kare örnekleyerek), zaman dökümünü ve gemini-istemi.md'deki istemi
   en yüksek düşünme ayarıyla gönderir.
4. Cevabı gemini-rapor.md olarak, ham yanıtı gemini-yanit.json olarak yazar.

API anahtarı koda ya da dosyaya yazılmaz. Bulut ortamında ağ vekili `x-goog-api-key` başlığını kayıtlı anahtarla
değiştirir; başka bir yerde çalıştırırken anahtarı GEMINI_API_KEY ortam değişkenine koy.

Kullanım: python3 gemini-gonder.py [video.mp4] [doküm.txt] [çıktı klasörü] [model (isteğe bağlı)]
"""
import json, os, ssl, sys, time, urllib.error, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
VIDEO = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else 'Basamak-tanitim.mp4')
DOKUM = os.path.abspath(sys.argv[2] if len(sys.argv) > 2 else 'Basamak-tanitim-dokum.txt')
OUT = os.path.abspath(sys.argv[3] if len(sys.argv) > 3 else os.path.dirname(VIDEO))
MODEL = sys.argv[4] if len(sys.argv) > 4 else None
BASE = 'https://generativelanguage.googleapis.com'
KEY = os.environ.get('GEMINI_API_KEY') or 'vekil-degistirir'   # bulutta vekil gerçek anahtarla değiştirir
CA = '/root/.ccr/ca-bundle.crt'
CTX = ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()


def call(method, url, body=None, headers=None, timeout=120, raw=False):
    h = {'x-goog-api-key': KEY}
    h.update(headers or {})
    data = body if isinstance(body, (bytes, type(None))) else json.dumps(body).encode('utf-8')
    if data is not None and 'Content-Type' not in h:
        h['Content-Type'] = 'application/json'
    req = urllib.request.Request(url, data=data, headers=h, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            return (r.headers, r.read()) if raw else json.loads(r.read() or b'{}')
    except urllib.error.HTTPError as e:
        msg = e.read().decode('utf-8', 'replace')[:800]
        raise SystemExit('Gemini %s %s -> %d: %s' % (method, url.split('?')[0], e.code, msg))


def pick_model():
    ms = call('GET', BASE + '/v1beta/models?pageSize=200').get('models', [])
    ok = [m['name'].split('/', 1)[1] for m in ms
          if 'generateContent' in m.get('supportedGenerationMethods', [])
          and '-pro' in m['name'] and not any(x in m['name'] for x in ('tts', 'image', 'vision', 'embedding', 'computer'))]
    if not ok:
        raise SystemExit('pro model bulunamadı: ' + ', '.join(m['name'] for m in ms)[:600])

    def rank(n):                      # gemini-3-pro > gemini-2.5-pro; kararlı sürüm önizlemeden önce
        import re
        v = re.search(r'gemini-(\d+(?:\.\d+)?)', n)
        return (float(v.group(1)) if v else 0, 'preview' not in n and 'exp' not in n, -len(n))
    ok.sort(key=rank, reverse=True)
    print('pro modeller:', ', '.join(ok[:6]))
    return ok[0]


def upload(path):
    size = os.path.getsize(path)
    hdr, _ = call('POST', BASE + '/upload/v1beta/files', {'file': {'display_name': os.path.basename(path)}},
                  {'X-Goog-Upload-Protocol': 'resumable', 'X-Goog-Upload-Command': 'start',
                   'X-Goog-Upload-Header-Content-Length': str(size), 'X-Goog-Upload-Header-Content-Type': 'video/mp4'}, raw=True)
    url = hdr.get('x-goog-upload-url') or hdr.get('X-Goog-Upload-URL')
    with open(path, 'rb') as f:
        data = f.read()
    _, body = call('POST', url, data, {'Content-Length': str(size), 'X-Goog-Upload-Offset': '0',
                                       'X-Goog-Upload-Command': 'upload, finalize', 'Content-Type': 'video/mp4'}, timeout=600, raw=True)
    fobj = json.loads(body)['file']
    print('yüklendi:', fobj['name'], '%.1f MB' % (size / 1e6))
    for _ in range(90):
        if fobj.get('state') == 'ACTIVE':
            return fobj
        if fobj.get('state') == 'FAILED':
            raise SystemExit('Gemini videoyu işleyemedi: ' + json.dumps(fobj)[:400])
        time.sleep(5)
        fobj = call('GET', BASE + '/v1beta/' + fobj['name'])
    raise SystemExit('video 7,5 dakikada hazır olmadı')


def prompt_text():
    s = open(os.path.join(HERE, 'gemini-istemi.md'), encoding='utf-8').read()
    parts = s.split('\n---\n')
    return parts[1].strip() if len(parts) >= 3 else s


def main():
    model = MODEL or pick_model()
    print('model:', model)
    f = upload(VIDEO)
    dokum = open(DOKUM, encoding='utf-8').read()
    think = {'thinkingLevel': 'high'} if 'gemini-3' in model else {'thinkingBudget': 32768}
    body = {
        'contents': [{'role': 'user', 'parts': [
            {'fileData': {'mimeType': 'video/mp4', 'fileUri': f['uri']}, 'videoMetadata': {'fps': 5}},
            {'text': 'Ek: Basamak-tanitim-dokum.txt\n\n' + dokum},
            {'text': prompt_text()},
        ]}],
        'generationConfig': {'maxOutputTokens': 32768, 'thinkingConfig': think, 'mediaResolution': 'MEDIA_RESOLUTION_HIGH'},
    }
    t = time.time()
    try:
        r = call('POST', BASE + '/v1beta/models/%s:generateContent' % model, body, timeout=1500)
    except SystemExit as e:                      # bazı modeller kare hızını ya da yüksek çözünürlüğü kabul etmez
        print('ilk deneme reddedildi, sade ayarla yeniden:', str(e)[:300])
        del body['contents'][0]['parts'][0]['videoMetadata']
        body['generationConfig'].pop('mediaResolution', None)
        r = call('POST', BASE + '/v1beta/models/%s:generateContent' % model, body, timeout=1500)
    json.dump(r, open(os.path.join(OUT, 'gemini-yanit.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    cand = (r.get('candidates') or [{}])[0]
    text = ''.join(p.get('text', '') for p in cand.get('content', {}).get('parts', []) if not p.get('thought'))
    if not text.strip():
        raise SystemExit('boş cevap: ' + json.dumps(r)[:800])
    head = '<!-- Gemini raporu · model: %s · süre: %d sn · bitiş nedeni: %s -->\n\n' % (model, time.time() - t, cand.get('finishReason'))
    open(os.path.join(OUT, 'gemini-rapor.md'), 'w', encoding='utf-8').write(head + text.strip() + '\n')
    u = r.get('usageMetadata', {})
    print('rapor yazıldı: %s · %d kelime · girdi %s, düşünme %s, çıktı %s token · bitiş %s' % (
        os.path.join(OUT, 'gemini-rapor.md'), len(text.split()), u.get('promptTokenCount'), u.get('thoughtsTokenCount'),
        u.get('candidatesTokenCount'), cand.get('finishReason')))
    try:
        call('DELETE', BASE + '/v1beta/' + f['name'])          # yüklenen video Gemini'de bırakılmaz
    except SystemExit:
        pass


if __name__ == '__main__':
    main()
