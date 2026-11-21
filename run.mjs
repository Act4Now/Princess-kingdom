import fs from 'node:fs';import assert from 'node:assert/strict';
const html=fs.readFileSync('index.html','utf8');const bank=JSON.parse(html.match(/const BANK=(\[.*?\]);\n/s)[1]);
assert.equal(bank.length,600);assert.equal(new Set(bank.map(x=>x.id)).size,600);
for(const cat of ['Desen','Mimă','Întrebare'])assert.equal(bank.filter(x=>x.cat===cat).length,200);
for(const cat of ['Desen','Mimă']){const rows=bank.filter(x=>x.cat===cat);assert.equal(new Set(rows.map(x=>x.task)).size,200);assert.ok(new Set(rows.map(x=>x.label)).size>=60);}
for(const c of bank){assert.ok(c.task&&c.taskEn);if(c.cat!=='Întrebare')assert.ok(c.emoji&&c.label&&c.labelEn);else assert.ok(c.answer&&c.answerEn);}
for(const id of ['read-aloud','skip-challenge','export-progress','import-progress','drawing-stamp','drawing-save','reset-stats'])assert.match(html,new RegExp('id="'+id+'"'));
assert.match(html,/speechSynthesis/);assert.match(html,/beforeinstallprompt/);assert.match(html,/pk-drawing-gallery/);
const manifest=JSON.parse(fs.readFileSync('manifest.webmanifest','utf8'));assert.equal(manifest.id,'./');assert.ok(manifest.icons.some(x=>x.purpose==='maskable'));
const v=fs.readFileSync('VERSION','utf8').trim();assert.equal(v,'38');assert.match(html,new RegExp('application-version" content="'+v+'"'));
console.log('Princess Kingdom source checks passed: 600 challenges, 200 per category, bilingual fields, feature hooks, PWA manifest and version.');
