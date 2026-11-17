// Basamak tanıtım kaydı, 2. adım: tanitim-kaydi.js çıktısından sesli MP4 üretir.
//  - Efektler: kayıtta çalan her ses, uygulamanın kendi ses kodu (SFX) ile aynı anına yerleştirilip çevrimdışı yeniden üretilir.
//  - İngilizce okuma: telefonda cihazın sesi okur; kayıtta yerine espeak-ng (en-gb) konur, okumanın kesildiği yerde kesilir.
//  - Üstte koyu bir şerit: bölüm adı, o anki adım ve süre sayacı. Uygulamanın ekranına dokunulmaz.
// Kullanım: node tanitim-birlestir.js [kayıt klasörü] [Basamak.html] [çıktı.mp4]
// Gerekenler: Node, Playwright'ın Chromium'u, ffmpeg (libx264, aac, drawtext), espeak-ng.
const { chromium } = require('playwright'); const fs=require('fs'), path=require('path'), cp=require('child_process');
const DIR=path.resolve(process.argv[2]||'tanitim');
const HTML=[process.argv[3],path.join(__dirname,'..','index.html'),path.join(__dirname,'uygulama','Basamak.html')].filter(Boolean).find(f=>fs.existsSync(f));
const OUTF=path.resolve(process.argv[4]||path.join(DIR,'Basamak-tanitim.mp4'));
const R=JSON.parse(fs.readFileSync(path.join(DIR,'kayit.json'),'utf8'));
const src=fs.readFileSync(HTML,'utf8');
const code=src.slice(src.indexOf('var AC=null,OUT=null,sfxN=0;'),src.indexOf('/* ---- sürpriz kutu:'));
if(code.length<1000)throw new Error('ses kodu bulunamadı');
const T0=R.frames[0][1]*1000, DUR=(R.end-T0)/1000+0.5;
const FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', FONTB='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf';
const W=780,H=1688,STRIP=172;
const tmp=path.join(DIR,'_birlestir'); fs.mkdirSync(tmp,{recursive:true});

(async()=>{
  // 1. okuma: her "speak" bir sonraki speak ya da stop anında kesilir
  const tts=[]; R.tts.forEach((e,i)=>{if(e.k!=='speak'||!e.s.trim())return;const nx=R.tts.slice(i+1).find(x=>x.t>e.t);tts.push({s:e.s,a:(e.t-T0)/1000,b:nx?(nx.t-T0)/1000:DUR})});
  tts.forEach((e,i)=>{const f=path.join(tmp,'tts'+i+'.wav');cp.execFileSync('espeak-ng',['-v','en-gb','-s','145','-a','150','-w',f,e.s]);
    const buf=fs.readFileSync(f);e.wav=buf.toString('base64');e.len=(buf.length-44)/(buf.readUInt32LE(28))});   // WAV başlığından süre
  // 2. efektler + okuma: çevrimdışı tek parça ses
  const b=await chromium.launch(); const p=await b.newPage(); await p.goto('about:blank');
  const wav64=await p.evaluate(async({code,sfx,tts,T0,DUR})=>{
    const SR=44100,off=new OfflineAudioContext(1,Math.ceil(SR*DUR),SR); let T=0;
    Object.defineProperty(off,'currentTime',{get:()=>T}); off.resume=()=>Promise.resolve();
    const api=new Function('PREF','window',code+';return {sfx:sfx};')({snd:1},{AudioContext:function(){return off}});
    for(const [name,arg,t] of sfx){T=Math.max(0,(t-T0)/1000);api.sfx(name,arg)}
    T=0;
    for(const e of tts){
      const bin=Uint8Array.from(atob(e.wav),c=>c.charCodeAt(0)).buffer, buf=await off.decodeAudioData(bin);
      const s=off.createBufferSource(),g=off.createGain(); s.buffer=buf; g.gain.value=0.8; s.connect(g); g.connect(off.destination);
      s.start(e.a+0.12); s.stop(Math.max(e.a+0.13,e.b));                       // telefondaki okuma da birkaç yüz ms gecikmeyle başlar
    }
    const out=await off.startRendering(), d=out.getChannelData(0), n=d.length;
    const ab=new ArrayBuffer(44+n*2), v=new DataView(ab), ws=(o,s)=>{for(let i=0;i<s.length;i++)v.setUint8(o+i,s.charCodeAt(i))};
    ws(0,'RIFF');v.setUint32(4,36+n*2,true);ws(8,'WAVE');ws(12,'fmt ');v.setUint32(16,16,true);v.setUint16(20,1,true);v.setUint16(22,1,true);
    v.setUint32(24,SR,true);v.setUint32(28,SR*2,true);v.setUint16(32,2,true);v.setUint16(34,16,true);ws(36,'data');v.setUint32(40,n*2,true);
    for(let i=0;i<n;i++){const x=Math.max(-1,Math.min(1,d[i]));v.setInt16(44+i*2,x<0?x*0x8000:x*0x7fff,true)}
    let s='';const u=new Uint8Array(ab);for(let i=0;i<u.length;i+=0x8000)s+=String.fromCharCode.apply(null,u.subarray(i,i+0x8000));return btoa(s);
  },{code,sfx:R.sfx,tts,T0,DUR});
  await b.close();
  fs.writeFileSync(path.join(tmp,'ses.wav'),Buffer.from(wav64,'base64'));
  // 3. kareler: değişken aralıklı kareler, süreleriyle
  let list='ffconcat version 1.0\n';
  R.frames.forEach(([f,ts],i)=>{const nx=i+1<R.frames.length?R.frames[i+1][1]:T0/1000+DUR;list+="file '"+path.join(DIR,'kareler',f)+"'\nduration "+Math.max(0.001,nx-ts).toFixed(4)+'\n'});
  list+="file '"+path.join(DIR,'kareler',R.frames[R.frames.length-1][0])+"'\n";
  fs.writeFileSync(path.join(tmp,'kareler.txt'),list);
  // 4. şerit: bölüm adı, adım, süre sayacı
  const sec=[],step=[];
  R.acts.forEach((a,i)=>{const t=Math.max(0,(a.t-T0)/1000);const nx=R.acts.slice(i+1).find(x=>a.adim?true:!x.adim);if(!a.adim)sec.push({t,s:a.bolum});else step.push({t,s:a.adim})});
  const span=(arr)=>arr.map((x,i)=>({a:x.t,b:i+1<arr.length?arr[i+1].t:DUR,s:x.s}));
  let k=0;const txt=s=>{const f=path.join(tmp,'t'+(k++)+'.txt');fs.writeFileSync(f,s);return f};
  const esc=f=>f.replace(/\\/g,'/').replace(/:/g,'\\:');
  let vf='[0:v]fps=30,scale='+W+':'+H+',pad='+W+':'+(H+STRIP)+':0:'+STRIP+':color=0x17132B';
  // 1. satır: kaydın adı ve süre sayacı; 2. satır: bölüm; 3. satır: o anki adım
  vf+=",drawtext=fontfile="+esc(FONT)+":textfile="+esc(txt('Basamak · tanıtım kaydı'))+":fontcolor=0xABA4D4:fontsize=24:x=28:y=20";
  vf+=",drawtext=fontfile="+esc(FONTB)+":text='%{eif\\:floor(t/60)\\:d\\:2}\\:%{eif\\:mod(floor(t)\\,60)\\:d\\:2}':fontcolor=0xABA4D4:fontsize=28:x=w-tw-28:y=17";
  span(sec).forEach(x=>{vf+=",drawtext=fontfile="+esc(FONTB)+":textfile="+esc(txt(x.s))+":fontcolor=white:fontsize=34:x=28:y=62:enable='between(t,"+x.a.toFixed(3)+","+x.b.toFixed(3)+")'"});
  span(step).forEach(x=>{vf+=",drawtext=fontfile="+esc(FONT)+":textfile="+esc(txt(x.s))+":fontcolor=0xFFD43B:fontsize=26:x=28:y=118:enable='between(t,"+x.a.toFixed(3)+","+x.b.toFixed(3)+")'"});
  vf+="[v]";
  fs.writeFileSync(path.join(tmp,'suzgec.txt'),vf);
  cp.execFileSync('ffmpeg',['-y','-loglevel','error','-f','concat','-safe','0','-i',path.join(tmp,'kareler.txt'),'-i',path.join(tmp,'ses.wav'),
    '-filter_complex_script',path.join(tmp,'suzgec.txt'),'-map','[v]','-map','1:a','-c:v','libx264','-preset','medium','-crf','21','-pix_fmt','yuv420p',
    '-c:a','aac','-b:a','160k','-t',DUR.toFixed(2),'-movflags','+faststart',OUTF],{stdio:'inherit'});
  // 5. döküm: hangi saniyede ne oldu, ne çaldı (değerlendirme için)
  const mm=t=>{const m=Math.floor(t/60),s=t-m*60;return String(m).padStart(2,'0')+':'+s.toFixed(1).padStart(4,'0')};
  const ev=[];
  R.acts.forEach(a=>ev.push([(a.t-T0)/1000,a.adim?'  '+a.adim:'## '+a.bolum]));
  R.sfx.forEach(([n,arg,t])=>ev.push([(t-T0)/1000,'    ses: '+n+(arg==null?'':' '+JSON.stringify(arg))]));
  tts.forEach(e=>{const cut=e.b-(e.a+0.12)<e.len-0.05;ev.push([e.a,'    okuma: "'+e.s+'" ('+(cut?(e.b-e.a-0.12).toFixed(1)+' sn sonra kesildi; tamamı '+e.len.toFixed(1)+' sn':e.len.toFixed(1)+' sn')+')'])});
  ev.sort((x,y)=>x[0]-y[0]);
  fs.writeFileSync(OUTF.replace(/\.mp4$/,'-dokum.txt'),'Basamak tanıtım kaydı · zaman dökümü (dakika:saniye)\n\n'+ev.map(e=>(e[1].startsWith('##')?'\n':'')+mm(Math.max(0,e[0]))+'  '+e[1]).join('\n')+'\n');
  console.log('hazır:',OUTF,(fs.statSync(OUTF).size/1e6).toFixed(1)+' MB',DUR.toFixed(1)+' sn');
})().catch(e=>{console.error('HATA',String(e.message||e).split('\n').slice(0,4).join(' | '));process.exit(2)});
