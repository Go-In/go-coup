function getCartItem(storage) {
  storage = storage || localStorage;
  return JSON.parse(storage.getItem('gocoup-cart')) || {};
}

function addItemToCart(cart, itemId) {
  cart[itemId] = cart[itemId] ? cart[itemId] + 1 : 1;
  return cart;
}

function handlerAddToCart(itemId, name) {
  var cart = getCartItem();
  var AddedCart = addItemToCart(cart, itemId);
  localStorage.setItem('gocoup-cart', JSON.stringify(cart));
  swal(
    'Add Success !',
    (AddedCart[itemId] + ' ' + name + ' ' + (AddedCart[itemId] ? ' tickets ' : ' ticket ') + 'in cart'),
    'success'
  )
}

function getCartUrl(storage) {
  storage = storage || localStorage;  
  var cartItems = getCartItem(storage);
  var keyItems = Object.keys(cartItems)
  return '/cart?cart=' + keyItems;
}

var goToCart = function() {
  var url = getCartUrl();
  document.location = url;
}

function cartItemToObject(storage) {
  storage = storage || localStorage;    
  var cartItems = getCartItem(storage);
  var keyItems = Object.keys(cartItems)
  var obj = keyItems.map(function(k) {
    return { 
      id: k,
      count: cartItems[k]
    }
  })
  return obj;
}

function incrementTicket(ticket_id) {
  var cartItems = getCartItem();
  cartItems = addItemToCart(cartItems, ticket_id)
  localStorage.setItem('gocoup-cart', JSON.stringify(cartItems));  
  renderTicket(ticket_id, cartItems[ticket_id]);
}

function renderTicket(ticket_id, quantity) {
  var numElement = document.getElementById('ticket_' + ticket_id);
  numElement.innerText = 'quantity: ' + quantity;
  $('#buy-btn').val(JSON.stringify(cartItemToObject()))
}

function decrementTicket(cart, ticket_id) {
  cart[ticket_id]--;
  return cart;
}

function ticketLeft(cart, ticket_id) {
  return cart[ticket_id] > 0;
}

function handlerDelete(ticket_id) {
  var cart = decrementTicket(getCartItem(), ticket_id);
  if (ticketLeft(cart, ticket_id)) {  
    localStorage.setItem('gocoup-cart', JSON.stringify(cart));
    renderTicket(ticket_id, cart[ticket_id]);
  } else {
    deleteTicketFromCart(ticket_id)
  }
}

function deleteTicketFromCart(ticket_id) {
  swal({
    title: 'เอา ticket นี้ออกจาก cart !',
    type: 'warning',
    showCancelButton: true,
    confirmButtonText: 'ใช่',
    cancelButtonText: 'ไม่',
  }).then(function() {
    var cartItems = getCartItem();
    delete cartItems[ticket_id];
    localStorage.setItem('gocoup-cart', JSON.stringify(cartItems));
    document.getElementById('row_' + ticket_id).remove();
    history.pushState(null, '', getCartUrl());
  })
}