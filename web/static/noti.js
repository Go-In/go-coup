function askPermission() {
  return new Promise(function(resolve, reject) {
    const permissionResult = Notification.requestPermission(function(result) {
      resolve(result);
    });

    if (permissionResult) {
      permissionResult.then(resolve, reject);
    }
  })
  .then(function(permissionResult) {
    if (permissionResult !== 'granted') {
      throw new Error('We weren\'t granted permission.');
    }
  });
}

function subscribeStore(storeId, userId) {
  askPermission()
  .then(function() {
    return navigator.serviceWorker.ready
  })
  .then(function(reg) {
    const subscribeOptions = {
      userVisibleOnly: true,
      applicationServerKey: urlBase64ToUint8Array('BAjY5Vq4p2wwLa-tdde3ip7uBxP02MN_4GTvQv4FDQTCs3b_tWl-eZoqtLhhtp_gPmvnk-CtS4zL4kRyeSb6f6I')
    }
    return reg.pushManager.subscribe(subscribeOptions)
  })
  .then(function() {
    console.log('sucess')
  })
}

function urlBase64ToUint8Array(base64String) {
  const padding = '='.repeat((4 - base64String.length % 4) % 4);
  const base64 = (base64String + padding)
    .replace(/\-/g, '+')
    .replace(/_/g, '/');

  const rawData = window.atob(base64);
  const outputArray = new Uint8Array(rawData.length);

  for (let i = 0; i < rawData.length; ++i) {
    outputArray[i] = rawData.charCodeAt(i);
  }
  return outputArray;
}

