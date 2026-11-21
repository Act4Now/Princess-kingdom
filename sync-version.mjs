import fs from 'node:fs';
const v=fs.readFileSync('VERSION','utf8').trim();
if(!/^\d+$/.test(v)) throw new Error('VERSION must be an integer');
const html=fs.readFileSync('index.html','utf8').replace(/(<meta name="application-version" content=")\d+(">)/,`$1${v}$2`).replace(/(id="footer-version" data-version=")\d+(">V)\d+(<\/span>)/,`$1${v}$2${v}$3`);
fs.writeFileSync('index.html',html);
fs.writeFileSync('version.txt',`V${v}\n`);
const meta=JSON.parse(fs.readFileSync('version.json','utf8'));meta.version=v;fs.writeFileSync('version.json',JSON.stringify(meta,null,2)+'\n');
const sw=fs.readFileSync('sw.js','utf8').replace(/princess-kingdom-v\d+[-a-z0-9]*/,'princess-kingdom-v'+v+'-release');fs.writeFileSync('sw.js',sw);
