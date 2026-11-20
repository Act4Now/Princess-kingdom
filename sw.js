/* Princess Kingdom V27 — synchronized version identifiers, offline-first launch. */
const CACHE_NAME = 'princess-kingdom-v27-version-sync';
const CACHE_PREFIX = 'princess-kingdom-';
const APP_FILES = [
  './', './index.html', './manifest.webmanifest', './version.json', './version.txt',
  './garden-extension.jpg', './icon-192.png', './icon-512.png'
];

self.addEventListener('install', event => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE_NAME);
    // Fetch a complete new app shell without waiting for the browser HTTP cache.
    await Promise.all(APP_FILES.map(async path => {
      const response = await fetch(new Request(path, { cache: 'reload' }));
      if (!response || !response.ok) throw new Error('Could not precache ' + path);
      await cache.put(path, response);
    }));
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

  const path = url.pathname;
  const isAppShell = request.mode === 'navigate' ||
    path.endsWith('/index.html') || path.endsWith('/manifest.webmanifest') ||
    path.endsWith('/version.json') || path.endsWith('/version.txt') || path.endsWith('/');

  event.respondWith((async () => {
    const cache = await caches.open(CACHE_NAME);
    const cached = await cache.match(request, { ignoreSearch: true }) ||
      (isAppShell ? await cache.match('./index.html') : null);

    // Serve the installed copy immediately. The registration code checks sw.js
    // separately in the background, so offline launch never waits for the network.
    if (cached) return cached;

    try {
      const response = await fetch(request);
      if (response && response.ok) await cache.put(request, response.clone());
      return response;
    } catch (error) {
      return isAppShell ? (await cache.match('./index.html')) || Response.error() : Response.error();
    }
  })());
});
