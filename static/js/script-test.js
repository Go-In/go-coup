export const getCartItem = (storage = localStorage) => {
  const data = storage.getItem('gocoup-cart') || '';
  const currentItems = data.split(',').filter(d => d !== '').map(d => JSON.parse(d));
  return currentItems;
}

export const cartItemToObject = (storage = localStorage) => {
  const cartItems = getCartItem(storage);
  const obj = cartItems.reduce((prev, curr) => {
    const ticket = {};
    const key = Object.keys(curr)[0];
    ticket.id = key;
    ticket.count = curr[key];
    prev.push(ticket);
    return prev;
  }, [])
  return obj;
}

export const getCartUrl = (storage = localStorage) => {
  const cartItems = getCartItem(storage);
  const keyItems = cartItems.map(c => Object.keys(c)[0])
  return `/cart?cart=${keyItems}`;
}
