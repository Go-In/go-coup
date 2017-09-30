const getCartItem = (storage = localStorage) => {
  const data = storage.getItem('gocoup-cart') || '';
  const currentItems = data.split(',').filter(d => d !== '');
  return currentItems;
}

const addItemToCart = (itemId) => {
  const cartItems = getCartItem();
  cartItems.push(itemId.toString());
  localStorage.setItem('gocoup-cart', [...new Set(cartItems)]);
  swal(
    'Success !',
    'เพิ่มสินค้าเข้าใน cart',
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
