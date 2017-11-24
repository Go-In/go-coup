var publicKey = 'BAjY5Vq4p2wwLa-tdde3ip7uBxP02MN_4GTvQv4FDQTCs3b_tWl-eZoqtLhhtp_gPmvnk-CtS4zL4kRyeSb6f6I'

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
      applicationServerKey: urlBase64ToUint8Array(publicKey)
    }
    return reg.pushManager.subscribe(subscribeOptions)
  })
  .then(function(subscription) {
    var endpoint = subscription.endpoint;
    var key = subscription.getKey('p256dh');
    var auth = subscription.getKey('auth');
    console.log(subscription)
    sendSubscriptionToServer(endpoint, key, auth);
  })
}

function sendSubscriptionToServer(endpoint, key, auth) {
  var encodedKey = btoa(String.fromCharCode.apply(null, new Uint8Array(key)));
  var encodedAuth = btoa(String.fromCharCode.apply(null, new Uint8Array(auth)));
  $.ajax({
    type: 'POST',
    url: 'http://localhost:8080/subscribe',
    data: {
      publicKey: encodedKey, 
      auth: encodedAuth, 
      endpoint: endpoint,        
    },
    success: function (response) {
      console.log('Subscribed successfully! ' + JSON.stringify(response));
    },
    error: function (err) {
      console.log('err', err)
    },
    dataType: 'json'
  });
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

navigator.serviceWorker.ready
.then(function(reg) {
  return reg.pushManager.getSubscription()
})
.then(function(subcribe) {
  if (subcribe) {
    renderUnSubscribeButton()
  } else {
    renderSubscribeButton()
  }
})

function renderSubscribeButton() {
  $('#subscribe-btn')
  .addClass('btn-primary')
  .removeClass('btn-danger')
  .html('subscribe this store')
}
function renderUnSubscribeButton() {
  $('#subscribe-btn')
  .addClass('btn-danger')
  .removeClass('btn-primary')
  .html('unsubscribe this store')
}
