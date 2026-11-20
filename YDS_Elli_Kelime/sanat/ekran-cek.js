// Basamak'ın bütün ana ekranlarını telefon boyutunda çeker (390x844, 2x; 29-34 koyu tema).
// Kullanım: node ekran-cek.js [Basamak.html] [çıktı klasörü]
//   varsayılan: ./uygulama/Basamak.html (pakette) ya da ../index.html (depoda), çıktı ./ekranlar
// Gerekenler: Node ve Playwright'ın Chromium'u (require('playwright')).
// Not: addInitScript içinde localStorage'a dokunma; sayfa bazı yüklemelerde boş depolamayla açılıyor. Durumu page.evaluate ile yaz.
const { chromium } = require('playwright'); const fs=require('fs'), path=require('path');
const cands=[process.argv[2],path.join(__dirname,'uygulama','Basamak.html'),path.join(__dirname,'..','index.html')].filter(Boolean);
const HTML=cands.find(f=>fs.existsSync(f)); if(!HTML){console.error('Basamak.html bulunamadı:',cands.join(', '));process.exit(1)}
const FILE='file://'+path.resolve(HTML), KEY='yds-elli-kelime-v1', out=path.resolve(process.argv[3]||path.join(process.cwd(),'ekranlar'));
fs.mkdirSync(out,{recursive:true});
const m=fs.readFileSync(HTML,'utf8').match(/var RAW=("(?:[^"\\]|\\.)*");/); if(!m){console.error('kelime listesi dosyada bulunamadı');process.exit(1)}
const W=JSON.parse(m[1]).trim().split('\n').map(l=>{const p=l.split('|');return{w:p[0],tr:p[2]}});
const BYW=Object.fromEntries(W.map(x=>[x.w,x])),BYTR=Object.fromEntries(W.map(x=>[x.tr,x]));
(async()=>{
  const b=await chromium.launch(); const done=[];
  const mk=async dark=>{const c=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2,colorScheme:dark?'dark':'light'});return c.newPage()};
  let p=await mk(false);
  const shot=async(name,full)=>{ try{ await p.waitForTimeout(250);
      if(full){const h=await p.evaluate(()=>{const b=document.querySelector('.body');return b?b.scrollHeight-b.clientHeight:0}); if(h>0){await p.setViewportSize({width:390,height:844+h+8});await p.waitForTimeout(150)}}
      await p.screenshot({path:out+'/'+name+'.png'}); if(full) await p.setViewportSize({width:390,height:844}); done.push(name);}catch(e){console.log('shot failed',name,e.message.split('\n')[0])} };
  const step=async(name,fn)=>{try{await fn()}catch(e){console.log('STEP FAILED',name,'-',e.message.split('\n')[0])}};
  const txt=s=>p.locator(s).first().innerText();
  const openMore=async()=>{await p.waitForSelector('details.demo');if(!(await p.locator('details.demo').evaluate(d=>d.open))){await p.click('details.demo summary');await p.waitForTimeout(200)}};
  const answer=async right=>{const x=BYW[(await txt('.hw')).trim()];const n=await p.locator('button.opt').count();for(let k=0;k<n;k++){const t=(await p.locator('button.opt .otxt').nth(k).innerText()).trim();if((t===x.tr)===right){await p.locator('button.opt').nth(k).click();await p.waitForSelector('.res');return}}};
  const intro=async()=>{const n=await p.locator('.idots i').count();for(let k=0;k<n;k++)await p.click('[data-act=inext]')};
  await step('home+words',async()=>{ await p.goto(FILE); await p.waitForSelector('.task'); await shot('01-bugun'); await p.click('[data-act=tab][data-v=words]'); await p.waitForSelector('details.demo'); await shot('02-kelime',true); });
  await step('word flow',async()=>{ await p.click('[data-act=start]'); await p.waitForSelector('[data-act=inext]'); await shot('03-tanitim-karti'); await intro(); await p.waitForSelector('button.opt'); await shot('04-soru');
    await answer(true); await shot('05-dogru',true); await p.click('[data-act=next]'); await answer(false); await shot('06-yanlis',true); await p.click('[data-act=next]');
    for(let k=0;k<3;k++){await answer(true);await p.click('[data-act=next]')} await p.waitForSelector('.match'); const c=p.locator('.chipm.en').first(); const id=await c.getAttribute('data-id'); await c.click(); await p.locator('.chipm:not(.en)[data-id="'+id+'"]').click(); await p.locator('.chipm.en:not([disabled])').first().click(); await shot('07-eslestirme');
    await p.locator('.chipm.en.sel').click(); const n=await p.locator('.chipm.en').count(); for(let k=0;k<n;k++){const e=p.locator('.chipm.en').nth(k); if(await e.isDisabled())continue; const i=await e.getAttribute('data-id'); await e.click(); await p.locator('.chipm:not(.en)[data-id="'+i+'"]').click()} await p.click('[data-act=next]');
    await intro(); for(let k=0;k<5;k++){await answer(true);await p.click('[data-act=next]')}
    await p.waitForSelector('#zone, [data-act=pickS]'); if(await p.locator('#zone').count()){ await p.locator('#bank .tile').first().click(); await p.locator('#bank .tile').first().click(); await shot('08-cumle-kurma'); while(await p.locator('#bank .tile').count()) await p.locator('#bank .tile').first().click(); await p.click('[data-act=check]'); } else { await shot('08-cumle-tamamlama'); await p.locator('[data-act=pickS]').first().click(); }
    await p.click('[data-act=next]'); await p.waitForSelector('.gbox'); await shot('09-surpriz-kutu'); for(let k=0;k<3;k++) await p.click('.gbox',{force:true}); await p.waitForSelector('.sky'); await shot('10-balon-patlat');
    for(let r=0;r<6;r++){ await p.waitForSelector('.sky .bal:not(.pop)'); const x=BYTR[(await txt('.meanbig')).trim()]; const m=await p.locator('.bal').count(); for(let k=0;k<m;k++){const bl=p.locator('.bal').nth(k); if((await bl.textContent()).trim()===x.w){await bl.click({force:true});break}} if(r<5) await p.waitForFunction(t=>{const e=document.querySelector('.meanbig');return e&&e.textContent.trim()!==t},x.tr); }
    await p.waitForSelector('.stkbig'); await p.waitForTimeout(1700); await shot('11-cikartma-odulu'); await p.click('[data-act=gdone]'); await p.waitForSelector('[data-act=inext], button.opt, .hzb, .turb, .swc, .mem, .sky'); });
  await step('settings, memory, summary',async()=>{ await p.click('[data-act=home]'); await openMore(); await shot('12-kelime-ayarlar-acik',true);
    await p.click('[data-act=trygift][data-f=mem]'); await p.waitForSelector('.mem'); await p.locator('.mc').nth(0).click(); await p.locator('.mc').nth(7).click(); await p.waitForTimeout(250); await shot('13-hafiza-kartlari'); await p.click('[data-act=home]');
    await p.click('[data-act=trymatch]'); await p.waitForSelector('.match'); await p.click('[data-act=home]');
    await p.click('[data-act=tryfmt][data-f=spell]'); await p.waitForSelector('#zone'); await p.locator('#bank .tile').first().click(); await shot('14-kelimeyi-kur'); await p.click('[data-act=home]');
    await p.click('[data-act=auto]'); await p.waitForSelector('.party'); await p.waitForTimeout(1700); await shot('15-gun-ozeti',true); });
  await step('album',async()=>{ await p.evaluate(k=>{const s=JSON.parse(localStorage.getItem(k));s.stk='sloth otter penguin owl fox unicorn t-rex octopus parrot hedgehog llama flamingo robot alien'.split(' ');s.rev+=5;localStorage.setItem(k,JSON.stringify(s))},KEY);
    await p.goto(FILE+'#kelime'); await p.reload(); await p.waitForSelector('details.demo'); await p.locator('details.card summary').first().click(); await p.waitForSelector('.album:visible'); await p.locator('.album').scrollIntoViewIfNeeded(); await shot('16-cikartma-albumu',true); });
  await step('grammar',async()=>{ await p.click('[data-act=tab][data-v=units]'); await p.waitForSelector('.urow'); await shot('17-gramer',true); await p.locator('.urow[data-act=unit]').first().click(); await p.waitForSelector('[data-act=gstart]'); await shot('18-unite',true);
    await p.locator('[data-act=gstart]').first().click(); await p.waitForSelector('[data-act=gpick]'); await shot('19-gramer-sorusu'); await p.locator('[data-act=gpick]').first().click(); await p.waitForSelector('[data-act=gnext]'); await shot('20-gramer-aciklama',true);
    for(let k=0;k<12;k++){ if(await p.locator('[data-act=gnext]').count()) await p.click('[data-act=gnext]'); if(await p.locator('.score').count()) break; await p.waitForSelector('[data-act=gpick], .score'); if(await p.locator('[data-act=gpick]').count()) await p.locator('[data-act=gpick]').nth(1).click(); }
    await p.waitForSelector('.score'); await shot('21-gramer-sonuc',true); });
  await step('connectors',async()=>{ await p.evaluate(()=>window.kelimeBack()); await p.click('[data-act=tab][data-v=units]'); await p.click('[data-act=bag]'); await p.waitForSelector('.gchip'); await shot('22-baglac-atolyesi',true);
    await p.locator('.gchip').first().click(); await p.waitForSelector('.bcard'); await shot('23-baglac-kartlari'); await p.evaluate(()=>window.kelimeBack()); await p.locator('[data-act=bsort]').first().click(); await p.waitForSelector('.stile'); await p.locator('.stile').first().click(); await shot('24-ayir-oyunu'); });
  await step('verb scan',async()=>{ await p.goto(FILE+'#kelime'); await p.reload(); await p.waitForSelector('[data-act=vhub]'); await p.click('[data-act=vhub]'); await p.waitForSelector('.vlv'); await shot('25-fiil-taramasi'); await p.click('.vlv[data-lv=B1]'); await p.waitForSelector('.hw'); await shot('26-fiil-sorusu');
    await p.click('[data-act=vidk]'); await p.waitForSelector('.res'); await shot('27-fiil-cevap'); await p.click('[data-act=vhub]'); await p.click('[data-act=tab][data-v=words]'); await openMore(); await p.click('[data-act=vauto]'); await p.waitForSelector('.vbar'); await shot('28-fiil-sonuc',true); });
  await step('dark',async()=>{ p=await mk(true); await p.goto(FILE); await p.waitForSelector('.task'); await shot('29-koyu-bugun'); await p.click('[data-act=tab][data-v=words]'); await shot('30-koyu-kelime',true);
    await p.click('[data-act=start]'); await p.waitForSelector('[data-act=inext]'); await shot('31-koyu-tanitim'); await intro(); await answer(true); await shot('32-koyu-dogru',true);
    await p.click('[data-act=home]'); await openMore(); await p.click('[data-act=trygift][data-f=bal]'); await p.waitForSelector('.sky'); await shot('33-koyu-balon'); await p.click('[data-act=home]'); await p.click('[data-act=tab][data-v=units]'); await p.waitForSelector('.urow'); await shot('34-koyu-gramer'); });
  console.log(done.length+' ekran ->',out); await b.close();
})();
