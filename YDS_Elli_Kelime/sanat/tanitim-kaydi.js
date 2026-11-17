// Basamak tanıtım kaydı, 1. adım: uygulamayı telefon boyunda (390x844, 2x) baştan sona oynatır.
// Her kareyi zamanıyla, çalan her sesi argümanıyla ve okunan her İngilizce metni zamanıyla kaydeder.
// 2. adım tanitim-birlestir.py: sesi yeniden üretir, okuyucu sesi ekler, üst şeridi çizer, MP4 yapar.
//
// Kullanım: node tanitim-kaydi.js [Basamak.html] [çıktı klasörü]
// Gerekenler: Node ve Playwright'ın Chromium'u.
// Not: addInitScript içinde localStorage'a dokunulmaz; sayfa bazı yüklemelerde boş depolamayla açılıyor.
const { chromium } = require('playwright'); const fs=require('fs'), path=require('path');
const cands=[process.argv[2],path.join(__dirname,'..','index.html'),path.join(__dirname,'uygulama','Basamak.html')].filter(Boolean);
const HTML=cands.find(f=>fs.existsSync(f)); if(!HTML){console.error('Basamak.html bulunamadı');process.exit(1)}
const OUT=path.resolve(process.argv[3]||'tanitim'); fs.mkdirSync(path.join(OUT,'kareler'),{recursive:true});
const src=fs.readFileSync(HTML,'utf8');
const js=re=>{const m=src.match(re);if(!m)throw new Error('veri bulunamadı: '+re);return JSON.parse(m[1])};
const W=js(/var RAW=("(?:[^"\\]|\\.)*");/).trim().split('\n').map(l=>{const p=l.split('|');return{w:p[0],tr:p[2],en:p[4],trs:p[5]}});
const V=js(/var VRAW=("(?:[^"\\]|\\.)*");/).trim().split('\n').map(l=>{const p=l.split('|');return{w:p[0],tr:p[2]}});
const GRAM=JSON.parse(src.match(/var GRAM=(\{[\s\S]*?\});\n/)[1]);
const BYW=Object.fromEntries(W.map(x=>[x.w,x])),BYTR=Object.fromEntries(W.map(x=>[x.tr,x])),VBY=Object.fromEntries(V.map(v=>[v.w,v]));
const norm=s=>s.replace(/----/g,'').replace(/[\[\]\s]/g,'');
const GQ={}; for(const id in GRAM.q)GRAM.q[id].forEach(r=>{GQ[norm(r[0])+'|'+r[1].slice().sort().join('|')]=r[1][r[2]]});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));

(async()=>{
  const b=await chromium.launch();
  const ctx=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2});
  await ctx.addInitScript(()=>{
    window.__sfxRec=[];window.__tts=[];
    // Android kabuğunun okuma köprüsünün yerine geçer: telefonda bu çağrıları cihazın sesi okur
    window.KelimeApp={speak:(t,r)=>{window.__tts.push({t:Date.now(),k:'speak',s:t})},stop:()=>{window.__tts.push({t:Date.now(),k:'stop'})}};
  });
  const p=await ctx.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  const cdp=await ctx.newCDPSession(p); const frames=[]; let fn=0;
  cdp.on('Page.screencastFrame',async f=>{
    const name=String(fn++).padStart(5,'0')+'.jpg';
    fs.writeFileSync(path.join(OUT,'kareler',name),Buffer.from(f.data,'base64'));
    frames.push([name,f.metadata.timestamp]);
    try{await cdp.send('Page.screencastFrameAck',{sessionId:f.sessionId})}catch(e){}
  });
  const acts=[]; let sec='';
  const bolum=(s)=>{sec=s;acts.push({t:Date.now(),bolum:s})};
  const adim=(s)=>{acts.push({t:Date.now(),bolum:sec,adim:s})};
  const txt=s=>p.locator(s).first().innerText();
  const tap=async(sel,o)=>{await p.locator(sel).first().click(o)};
  const right=async()=>{const x=BYW[(await txt('.hw')).trim()];const n=await p.locator('button.opt').count();for(let k=0;k<n;k++){if((await p.locator('button.opt .otxt').nth(k).innerText()).trim()===x.tr)return k}return 0};
  const pick=async(ok)=>{const k=await right();await p.locator('button.opt').nth(ok?k:(k+1)%5).click();await p.waitForSelector('.res')};

  await p.goto('file://'+path.resolve(HTML)); await p.waitForSelector('.task');
  await cdp.send('Page.startScreencast',{format:'jpeg',quality:88,maxWidth:780,maxHeight:1688,everyNthFrame:1});
  await sleep(400);
  bolum('Bugün ekranı'); adim('Uygulama açıldı: bugünün iki görevi'); await sleep(2600);

  bolum('Kelime turu · tanıtım kartları'); adim('Kelime görevine dokunuldu'); await tap('[data-act=start]'); await p.waitForSelector('[data-act=inext]');
  for(let k=0;k<5;k++){
    adim('Tanıtım kartı '+(k+1)+'/5 · kelime kendiliğinden okunur'); await sleep(2100);
    if(k===2){adim('Önceki karta dönüldü');await tap('[data-act=iprev]');await sleep(1500);adim('Yeniden ileri');await tap('[data-act=inext]');await sleep(1300)}
    await tap('[data-act=inext]');
  }
  bolum('Kelime turu · sorular');
  const plan=[['doğru',1],['doğru',1],['doğru (3. üst üste)',1],['yanlış',0],['Bilmiyorum',-1]];
  for(let k=0;k<plan.length;k++){
    await p.waitForSelector('button.opt'); adim('Soru '+(k+1)+': '+plan[k][0]); await sleep(1500);
    if(plan[k][1]<0){await tap('[data-act=idk]');await p.waitForSelector('.res')}else await pick(plan[k][1]===1);
    await sleep(1700);
    if(k===1){adim('Hoparlöre dokunuldu: kelime ve cümle okunur');await tap('.spk');await sleep(1400);adim('Okuma sürerken Devam: okuma kesilir')}
    await tap('[data-act=next]');
  }
  bolum('Ara görev · eşleştirme'); await p.waitForSelector('.match'); adim('Eşleştirme turu açıldı'); await sleep(1500);
  {const n=await p.locator('.chipm.en').count();let miss=true;
   for(let k=0;k<n;k++){const c=p.locator('.chipm.en').nth(k);const id=await c.getAttribute('data-id');await c.click();await sleep(550);
     if(miss){miss=false;adim('Yanlış eşleşme denemesi');await p.locator('.chipm:not(.en):not([data-id="'+id+'"]):not([disabled])').first().click();await sleep(900);await c.click();await sleep(450)}
     adim('Doğru çift');await p.locator('.chipm:not(.en)[data-id="'+id+'"]').click();await sleep(700)}}
  adim('Eşleştirme bitti'); await sleep(1600); await tap('[data-act=next]');
  bolum('Kelime turu · tanıtım kartları'); await p.waitForSelector('[data-act=inext]');
  for(let k=0;k<5;k++){adim('Tanıtım kartı '+(k+1)+' / 5');await sleep(1250);await tap('[data-act=inext]')}
  bolum('Kelime turu · sorular');
  for(let k=0;k<5;k++){await p.waitForSelector('button.opt');adim('Soru '+(k+6)+': '+(k===2?'yanlış':'doğru'));await sleep(1100);await pick(k!==2);await sleep(1300);await tap('[data-act=next]')}
  bolum('Ara görev · cümle kurma'); await p.waitForSelector('#zone, [data-act=pickS]'); adim('Cümle görevi açıldı'); await sleep(1800);
  if(await p.locator('#zone').count()){
    // parçaları doğru sırayla dizer: doğru sıra kelime listesindeki cümleden okunur
    const trs=(await p.evaluate(()=>document.querySelector('.trbig').textContent.trim())), row=W.find(w=>w.trs===trs);
    const parts=row?row.en.split(' / ').map((c,i,a)=>{c=c.replace(/[\[\]]/g,'');if(i===0&&!/^I\b/.test(c))c=c.charAt(0).toLowerCase()+c.slice(1);if(i===a.length-1)c=c.replace(/\.$/,'');return c}):null;
    for(let k=0;k<4;k++){
      const n=await p.locator('#bank .tile').count();let hit=false;
      if(parts)for(let j=0;j<n;j++){if((await p.locator('#bank .tile').nth(j).innerText()).trim()===parts[k]){adim('Parça yerleştirildi');await p.locator('#bank .tile').nth(j).click();hit=true;break}}
      if(!hit){adim('Parça yerleştirildi');await p.locator('#bank .tile').first().click()}
      await sleep(750);
    }
    await sleep(500); adim('Kontrol et'); await tap('[data-act=check]');
  }else{adim('Cümlenin devamı seçildi');await p.locator('[data-act=pickS]').first().click()}
  await sleep(2200); await tap('[data-act=next]');

  bolum('Sürpriz kutu'); await p.waitForSelector('.gbox'); adim('Kutu çıktı'); await sleep(1800);
  for(let k=1;k<=3;k++){adim('Kutuya dokunuş '+k);await tap('.gbox',{force:true});await sleep(k<3?1100:300)}
  bolum('Sürpriz oyun · balon patlat'); await p.waitForSelector('.sky'); adim('Oyun açıldı'); await sleep(1300);
  for(let r=0;r<6;r++){
    await p.waitForSelector('.sky .bal:not(.pop)'); const x=BYTR[(await txt('.meanbig')).trim()]; adim('Balon '+(r+1)+' / 6'); await sleep(1100);
    if(r===1){adim('Yanlış balon');await p.locator('.bal').filter({hasNotText:x.w}).first().click({force:true});await sleep(1000)}
    const n=await p.locator('.bal').count(); for(let k=0;k<n;k++){const bl=p.locator('.bal').nth(k);if((await bl.textContent()).trim()===x.w){adim('Doğru balon');await bl.click({force:true});break}}
    if(r<5)await p.waitForFunction(t=>{const e=document.querySelector('.meanbig');return e&&e.textContent.trim()!==t},x.tr);
  }
  bolum('Ödül · çıkartma'); await p.waitForSelector('.stkbig'); adim('Çıkartma kazanıldı (adı okunur)'); await sleep(3800);
  await tap('[data-act=gdone]'); await sleep(900);

  bolum('Demo aracı · günün kalanı otomatik'); adim('Kelime ekranına dönüldü'); await tap('.top .x'); await p.waitForSelector('details.demo'); await sleep(1200);
  adim('Ayarlar ve deneme açıldı'); await tap('details.demo summary'); await sleep(1300);
  await p.locator('[data-act=auto]').scrollIntoViewIfNeeded(); await sleep(700); adim('Bugünü otomatik bitir'); await tap('[data-act=auto]');
  bolum('Gün özeti'); await p.waitForSelector('.party'); adim('Gün bitti: özet ve kutlama'); await sleep(3600);
  bolum('Kelime ekranı · gün serisi'); adim('Ana sayfaya dönüldü: seri arttı'); await tap('.foot [data-act=home]'); await sleep(2600);

  bolum('Günün grameri'); adim('Bugün sekmesi'); await tap('[data-act=tab][data-v=home]'); await sleep(1500); adim('Gramer görevine dokunuldu'); await tap('[data-act=gdaily]');
  for(let k=0;k<3;k++){
    await p.waitForSelector('button.opt'); const d=await p.evaluate(()=>({q:document.querySelector('.gq').innerText,os:[...document.querySelectorAll('button.opt .otxt')].map(n=>n.innerText.trim())}));
    const ans=GQ[norm(d.q)+'|'+d.os.slice().sort().join('|')]; const ok=k!==1; const i=ans!=null?(ok?d.os.indexOf(ans):d.os.findIndex(o=>o!==ans)):0;
    adim('Gramer sorusu '+(k+1)+': '+(ok?'doğru':'yanlış')); await sleep(2200); await p.locator('button.opt').nth(Math.max(0,i)).click(); await p.waitForSelector('.res'); await sleep(2300); await tap('[data-act=gnext]');
  }
  await sleep(900); adim('Gramerden çıkıldı');
  for(let k=0;k<4&&!(await p.locator('.tabs').count());k++){await tap('.top .x');await sleep(900)}

  bolum('Fiil taraması'); await tap('[data-act=tab][data-v=words]'); await sleep(900); adim('Fiil taraması açıldı'); await tap('[data-act=vhub]'); await sleep(2000);
  adim('B1 fiilleri'); await tap('.vlv[data-lv=B1]');
  for(let k=0;k<5;k++){
    await p.waitForSelector('.hw'); const w=(await txt('.hw')).trim(); const t=VBY[w].tr; const ok=k!==3; adim('Fiil '+(k+1)+': '+(ok?'doğru':'yanlış')); await sleep(1300);
    const n=await p.locator('button.opt').count(); let i=0; for(let j=0;j<n;j++){if(((await p.locator('button.opt .otxt').nth(j).innerText()).trim()===t)===ok){i=j;break}}
    await p.locator('button.opt').nth(i).click(); await p.waitForSelector('.res');
    if(ok)await p.waitForFunction(w=>{const e=document.querySelector('.hw');return e&&e.textContent.trim()!==w||!!document.querySelector('.party')},w,{timeout:5000});
    else{await sleep(1800);await tap('[data-act=vnext]')}
  }
  await sleep(800); adim('Taramaya dönüldü'); await tap('.top .x'); await sleep(2000);

  bolum('Çıkartma albümü'); await tap('.top .x'); await p.waitForSelector('details.demo'); await sleep(800);
  const alb=p.locator('details.card summary').first(); await alb.scrollIntoViewIfNeeded(); adim('Albüm açıldı'); await alb.click(); await sleep(400); await p.locator('.album').scrollIntoViewIfNeeded(); await sleep(2400);

  bolum('Koyu tema'); adim('Telefon koyu temaya geçti'); await p.emulateMedia({colorScheme:'dark'}); await sleep(1800); await tap('[data-act=tab][data-v=home]'); await sleep(2400);
  await cdp.send('Page.stopScreencast'); await sleep(300);
  const rec=await p.evaluate(()=>({sfx:window.__sfxRec,tts:window.__tts,now:Date.now()}));
  fs.writeFileSync(path.join(OUT,'kayit.json'),JSON.stringify({frames,sfx:rec.sfx,tts:rec.tts,acts,end:rec.now},null,0));
  console.log('kare',frames.length,'| ses',rec.sfx.length,'| okuma',rec.tts.filter(x=>x.k==='speak').length,'| süre',((rec.now-frames[0][1]*1000)/1000).toFixed(1)+' sn','| ilk kare - ilk adım (ms)',Math.round(acts[0].t-frames[0][1]*1000));
  if(errs.length)console.log('sayfa hataları',errs);
  await b.close();
})().catch(e=>{console.error('HATA',e.message.split('\n').slice(0,3).join(' | '));process.exit(2)});
