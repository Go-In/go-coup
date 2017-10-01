export const getCartItem = (storage = localStorage) => {
  return JSON.parse(storage.getItem('gocoup-cart')) || {};
}

export const addItemToCart = (cart, itemId) => {
  cart[itemId] = cart[itemId] ? cart[itemId] + 1 : 1;
  return cart;
}

export const getCartUrl = (storage = localStorage) => {
  const cartItems = getCartItem(storage);
  const keyItems = Object.keys(cartItems)
  return `/cart?cart=${keyItems}`;
}

function decrementTicket(cart, ticket_id) {
  var item = cart.find(c => Object.keys(c)[0] === String(ticket_id));
  item[ticket_id]--;
  return [...cart, item];
}

function ticketLeft(cart, ticket_id) {
  return cart.find(c => c[String(ticket_id)] > 0);
}
