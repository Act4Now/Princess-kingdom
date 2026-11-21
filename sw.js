/* Princess Kingdom V34 — combined randomization, responsive, bilingual UI and local stats release. */
const CACHE_NAME = 'princess-kingdom-v34-full-english-drawing-tools';
const CACHE_PREFIX = 'princess-kingdom-';
const APP_FILES = ['./','./index.html','./manifest.webmanifest','./version.json','./version.txt','./garden-extension.jpg','./icon-192.png','./icon-512.png'];
self.addEventListener('install', event => {
 event.waitUntil((async()=>{
  const cache=await caches.open(CACHE_NAME);
  // A failed fetch aborts this install and leaves the previous active worker untouched.
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
 const path=url.pathname;
 const shell=request.mode==='navigate'||path.endsWith('/index.html')||path.endsWith('/manifest.webmanifest')||path.endsWith('/version.json')||path.endsWith('/version.txt')||path.endsWith('/');
 event.respondWith((async()=>{
  const cache=await caches.open(CACHE_NAME);
  const cached=await cache.match(request,{ignoreSearch:true})||(shell?await cache.match('./index.html'):null);
  if(cached)return cached;
  try{const response=await fetch(request);if(response&&response.ok)await cache.put(request,response.clone());return response;}
  catch(error){return shell?(await cache.match('./index.html'))||Response.error():Response.error();}
 })());
});
