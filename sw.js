/* Princess Kingdom V23 — automatic updates + reliable offline fallback. */
const CACHE_NAME = 'princess-kingdom-v23-footer-background';
const CACHE_PREFIX = 'princess-kingdom-';
const APP_FILES = [
  './',
  './index.html',
  './manifest.webmanifest',
  './icon-192.png',
  './icon-512.png'
];

self.addEventListener('install', event => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE_NAME);
    await cache.addAll(APP_FILES);
    await self.skipWaiting();
  })());
});

self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    const names = await caches.keys();
    await Promise.all(names
      .filter(name => name.startsWith(CACHE_PREFIX) && name !== CACHE_NAME)
      .map(name => caches.delete(name)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', event => {
  const request = event.request;
  if (request.method !== 'GET') return;

  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return;

  const isAppShell = request.mode === 'navigate' ||
    url.pathname.endsWith('/index.html') ||
    url.pathname.endsWith('/manifest.webmanifest') ||
    url.pathname.endsWith('/');

  if (isAppShell) {
    // Network-first, bypassing the browser HTTP cache for the app shell.
    event.respondWith((async () => {
      const cache = await caches.open(CACHE_NAME);
      try {
        const fresh = await fetch(request, { cache: 'no-store' });
        if (fresh && fresh.ok) {
          await cache.put(request, fresh.clone());
        }
        return fresh;
      } catch (error) {
        return (await caches.match(request)) ||
          (await caches.match('./index.html')) ||
          Response.error();
      }
    })());
    return;
  }

  // Cache-first for icons and other static resources; update the cache in the background.
  event.respondWith((async () => {
    const cache = await caches.open(CACHE_NAME);
    const cached = await cache.match(request);
    if (cached) return cached;
    try {
      const response = await fetch(request);
      if (response && response.ok) await cache.put(request, response.clone());
      return response;
    } catch (error) {
      return Response.error();
    }
  })());
});
