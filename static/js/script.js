const getCartItem = () => {
  const data = localStorage.getItem('gocoup-cart') || '';
  const currentItems = data.split(',').filter(d => d !== '');
  console.log(currentItems);
  return currentItems;
}

const addItemToCart = (itemId) => {
  const cartItems = getCartItem();
  cartItems.push(itemId.toString());
  localStorage.setItem('gocoup-cart', [...new Set(cartItems)]);
}

const goToCart = () => {
  const cartItems = getCartItem();
  document.location = `/cart?cart=${cartItems}`;
}
