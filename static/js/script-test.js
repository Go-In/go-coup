export const getCartItem = (storage = localStorage) => {
  const data = storage.getItem('gocoup-cart') || '';
  const currentItems = data.split(',').filter(d => d !== '').map(d => JSON.parse(d));
  return currentItems;
}

export const getCartUrl = (storage = localStorage) => {
  const cartItems = getCartItem(storage);
  const keyItems = cartItems.map(c => Object.keys(c)[0])
  return `/cart?cart=${keyItems}`;
}
