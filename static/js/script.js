const getCartItem = (storage = localStorage) => {
  const data = storage.getItem('gocoup-cart') || '';
  const currentItems = data.split(',').filter(d => d !== '').map(d => JSON.parse(d));
  return currentItems;
}

const addItemToCart = (itemId, name) => {
  let cartItems = getCartItem();
  const item = cartItems.find(c => Object.keys(c)[0] === String(itemId))
  if (item) {
    item[itemId]++;
    cartItems = [...cartItems, item];
  } else {
    cartItems.push({[itemId]: 1})
  }
  const cartString = cartItems.map(c => JSON.stringify(c))
  localStorage.setItem('gocoup-cart', [...new Set(cartString)]);
  swal(
    'Add Success !',
    ((item ? item[itemId] : 1) + ' ' + name + ' ' + (item ? ' tickets ' : ' ticket ') + 'in cart'),
    'success'
  )
}

const getCartUrl = (storage = localStorage) => {
  const cartItems = getCartItem(storage);
  return `/cart?cart=${cartItems}`;
}

const goToCart = () => {
  const url = getCartUrl();
  document.location = url;
}
