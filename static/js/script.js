const addItemToCart = (itemId) => {
  const data = localStorage.getItem('gocoup-cart') || '';
  const currentItems = data.split(',').filter(d => d !== '');
  console.log(currentItems);
  currentItems.push(itemId.toString());
  localStorage.setItem('gocoup-cart', [...new Set(currentItems)]);
}

const goToCart = () => {
  const data = localStorage.getItem('gocoup-cart') || '';
  const currentItems = data.split(',').filter(d => d !== '');
  console.log(currentItems);
  document.location = `cart.html?cart=${currentItems}`;
}
