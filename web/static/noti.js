var publicKey = 'BAjY5Vq4p2wwLa-tdde3ip7uBxP02MN_4GTvQv4FDQTCs3b_tWl-eZoqtLhhtp_gPmvnk-CtS4zL4kRyeSb6f6I'
var host = 'localhost'

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

function subscribeStore() {
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
    sendSubscriptionToServer({
      endpoint,
      publicKey: btoa(String.fromCharCode.apply(null, new Uint8Array(key))),
      auth: btoa(String.fromCharCode.apply(null, new Uint8Array(auth))),
      userId: $('#userId').attr('value'),
      storeId: $('#storeId').attr('value')
    });
  })
}

function sendUnSubscriptionToServer() {
  $.ajax({
    type: 'POST',
    url: 'http://' + host + ':8080/unsubscribe',
    data: {
      userId: $('#userId').attr('value'),
      storeId: $('#storeId').attr('value'),
    },
    success: function (response) {
      console.log('Unsubscribed successfully! ' + JSON.stringify(response));      
      if (response.success) {
        renderSubscribeButton()
      }
    },
    error: function (err) {
      console.log('err', err)
    },
    dataType: 'json'
  })
}

function sendSubscriptionToServer(data) {
  $.ajax({
    type: 'POST',
    url: 'http://' + host + ':8080/subscribe',
    data,
    success: function (response) {
      console.log('Subscribed successfully! ' + JSON.stringify(response));
      if (response.success) {
        renderUnSubscribeButton()
      }
    },
    error: function (err) {
      console.log('err', err)
    },
    dataType: 'json'
  });
}

function checkSubscribe() {
  let userId = $('#userId').attr('value')
  let storeId = $('#storeId').attr('value')
  $.ajax({
    type: 'GET',
    url: 'http://' + host + ':8080/subscribe/check/' + userId + '/' + storeId,
    success: function (isSub) {
      if (isSub) {
        renderUnSubscribeButton()
      } else {
        renderSubscribeButton()
      }
    }
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

// navigator.serviceWorker.ready
// .then(function(reg) {
//   return reg.pushManager.getSubscription()
// })
// .then(function(subcribe) {
//   if (subcribe) {
//     renderUnSubscribeButton()
//   } else {
//     renderSubscribeButton()
//   }
// })

function renderSubscribeButton() {
  $('#subscribe-btn')
  .html('<i class="fa fa-thumbs-up" aria-hidden="true"></i>' + '  subscribe this store')
  .attr('onclick', 'subscribeStore()')
}

function renderUnSubscribeButton() {
  $('#subscribe-btn')
  .html('<i class="fa fa-thumbs-down" aria-hidden="true"></i>' + '  unsubscribe this store')
  .attr('onclick', 'sendUnSubscriptionToServer()')
}
if (window.location.href.split('/')[3] === 'detail') {
  checkSubscribe()
}