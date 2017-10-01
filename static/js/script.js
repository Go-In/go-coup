const getCartItem = (storage = localStorage) => {
  return JSON.parse(storage.getItem('gocoup-cart')) || {};
}

const addItemToCart = (cart, itemId) => {
  cart[itemId] = cart[itemId] ? cart[itemId] + 1 : 1;
  return cart;
}

const handlerAddToCart = (itemId, name) => {
  const cart = getCartItem();
  const AddedCart = addItemToCart(cart, itemId);
  console.log(AddedCart);
  localStorage.setItem('gocoup-cart', JSON.stringify(cart));
  swal(
    'Add Success !',
    (AddedCart[itemId] + ' ' + name + ' ' + (AddedCart[itemId] ? ' tickets ' : ' ticket ') + 'in cart'),
    'success'
  )
}

const getCartUrl = (storage = localStorage) => {
  const cartItems = getCartItem(storage);
  const keyItems = Object.keys(cartItems)
  return `/cart?cart=${keyItems}`;
}

const goToCart = () => {
  const url = getCartUrl();
  document.location = url;
}

const cartItemToObject = (storage = localStorage) => {
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
