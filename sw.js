/* Princess Kingdom V50 — offline-first app shell. */
const CACHE_NAME = 'princess-kingdom-v51-release';
const CACHE_PREFIX = 'princess-kingdom-';
const APP_FILES = ["./","./index.html","./v50-enhancements.js","./manifest.webmanifest","./version.json","./version.txt","./scene.jpg?v=50","./music.mp3?v=50","./icon-192.png","./icon-512.png","./icon-maskable-512.png","./princess-anna.webp","./princess-ariel.webp","./princess-aurora.webp","./princess-belle.webp","./princess-cinderella.webp","./princess-eilonwy.webp","./princess-elena-of-avalor.webp","./princess-elsa.webp","./princess-flower-tale.webp","./princess-giselle.webp","./princess-jasmine.webp","./princess-kida.webp","./princess-megara.webp","./princess-merida.webp","./princess-moana.webp","./princess-mulan.webp","./princess-pocahontas.webp","./princess-rapunzel-from-the-tale.webp","./princess-rapunzel.webp","./princess-raya.svg","./princess-snow-white.webp","./princess-sofia.webp","./princess-the-brave-princess.webp","./princess-the-butterfly-princess.webp","./princess-the-crystal-princess.webp","./princess-the-dancing-princess.webp","./princess-the-dream-princess.webp","./princess-the-enchanted-castle-princess.webp","./princess-the-forest-princess.webp","./princess-the-frog-princess.webp","./princess-the-ice-princess.webp","./princess-the-moon-princess.webp","./princess-the-pearl-princess.webp","./princess-the-princess-and-the-pea.webp","./princess-the-princess-and-the-unicorn.webp","./princess-the-princess-of-hearts.webp","./princess-the-rainbow-princess.webp","./princess-the-rose-princess.webp","./princess-the-sea-princess.webp","./princess-the-secret-garden-princess.webp","./princess-the-singing-princess.webp","./princess-the-snow-princess.webp","./princess-the-star-princess.webp","./princess-the-storybook-princess.webp","./princess-the-sun-princess.webp","./princess-the-swan-princess.webp","./princess-the-tower-princess.webp","./princess-the-traveling-princess.webp","./princess-tiana.webp","./princess-vanellope.webp","./princess-fallback.svg"];
self.addEventListener('install', event => {
 event.waitUntil((async()=>{
  const cache=await caches.open(CACHE_NAME);
  // A failed fetch aborts the install and leaves the previous worker untouched.
  for(const path of APP_FILES){
   const response=await fetch(new Request(path,{cache:'reload'}));
   if(!response||!response.ok)throw new Error('Could not precache '+path);
   await cache.put(path,response);
  }
  await self.skipWaiting();
 })());
});
self.addEventListener('activate',event=>{event.waitUntil((async()=>{
 const names=await caches.keys();
 await Promise.all(names.filter(n=>n.startsWith(CACHE_PREFIX)&&n!==CACHE_NAME).map(n=>caches.delete(n)));
 await self.clients.claim();
})());});
self.addEventListener('fetch',event=>{
 const request=event.request;if(request.method!=='GET')return;
 const url=new URL(request.url);if(url.origin!==self.location.origin)return;
 const shell=request.mode==='navigate';
 event.respondWith((async()=>{
  const cache=await caches.open(CACHE_NAME);
  const cached=await cache.match(request,{ignoreSearch:true})||(shell?await cache.match('./index.html'):null);
  if(cached){
   const range=request.headers.get('range');
   if(range&&cached.status===200){
    const m=/bytes=(\d*)-(\d*)/.exec(range);
    const blob=await cached.blob();
    const start=m&&m[1]?parseInt(m[1],10):0;
    const end=m&&m[2]?Math.min(parseInt(m[2],10),blob.size-1):blob.size-1;
    return new Response(blob.slice(start,end+1),{status:206,headers:{'Content-Type':cached.headers.get('Content-Type')||'audio/mpeg','Content-Range':'bytes '+start+'-'+end+'/'+blob.size,'Content-Length':String(end-start+1),'Accept-Ranges':'bytes'}});
   }
   return cached;
  }
  try{return await fetch(request);}catch(e){if(shell){const fallback=await cache.match('./index.html');if(fallback)return fallback;}throw e;}
 })());
});
