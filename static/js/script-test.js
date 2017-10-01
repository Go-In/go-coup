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

export const cartItemToObject = (storage = localStorage) => {
  const cartItems = getCartItem(storage);
  const keyItems = Object.keys(cartItems)
  const obj = keyItems.map(k => {
    return { 
      id: k,
      count: cartItems[k]
    }
  })
  return obj;
}


export function decrementTicket(cart, ticket_id) {
  cart[ticket_id]--;
  return cart;
}

export function ticketLeft(cart, ticket_id) {
  return cart[ticket_id] > 0;
}