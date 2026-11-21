/* Princess Kingdom V44 — offline-first app shell. */
const CACHE_NAME = 'princess-kingdom-v44-release';
const CACHE_PREFIX = 'princess-kingdom-';
const APP_FILES = ['./','./index.html','./manifest.webmanifest','./version.json','./version.txt','./scene.jpg?v=44','./music.mp3?v=44','./icon-192.png','./icon-512.png','./icon-maskable-512.png'];
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
  // Range requests (audio seeking) are answered from the full cached file.
  const cached=await cache.match(request,{ignoreSearch:true})||(shell?await cache.match('./index.html'):null);
  if(cached){
   const range=request.headers.get('range');
   if(range&&cached.status===200){
    // Safari requires 206 answers for media; serve the requested slice of the cached file.
    const m=/bytes=(\d*)-(\d*)/.exec(range);
    const blob=await cached.blob();
    const start=m&&m[1]?parseInt(m[1],10):0;
    const end=m&&m[2]?Math.min(parseInt(m[2],10),blob.size-1):blob.size-1;
    return new Response(blob.slice(start,end+1),{status:206,headers:{'Content-Type':cached.headers.get('Content-Type')||'audio/mpeg','Content-Range':'bytes '+start+'-'+end+'/'+blob.size,'Content-Length':String(end-start+1)}});
   }
   return cached;
  }
  try{const response=await fetch(request);if(response&&response.ok&&response.status===200)await cache.put(request,response.clone());return response;}
  catch(error){return shell?(await cache.match('./index.html'))||Response.error():Response.error();}
 })());
});
