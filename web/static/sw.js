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
  const data = event.data.json()
  const { title, message, image } = data
  const options = {
    body: message,
    icon: image
  };
  event.waitUntil(self.registration.showNotification(title, options));
});