importScripts('/static/sw-toolbox/sw-toolbox.js');

self.addEventListener('install', function(event) {
  self.skipWaiting();
});
self.addEventListener('activate', function(event) {
  event.waitUntil(self.clients.claim());
});

toolbox.precache(['/', '/user/coupon']);

toolbox.router.get('/static*', toolbox.networkFirst);

toolbox.router.get('/', toolbox.networkFirst);
toolbox.router.get('/user/coupon', toolbox.networkFirst);


self.addEventListener('push', function(event) {
  const title = 'Push Codelab';
  const options = {
    body: 'Yay it works.',
    icon: 'images/icon.png',
    badge: 'images/badge.png'
  };
  event.waitUntil(self.registration.showNotification(title, options));
});