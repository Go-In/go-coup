import { expect } from 'chai';
import {
  getCartItem,
  addItemToCart,
  getCartUrl,
  cartItemToObject,
  decrementTicket
} from './script-test';

describe('simple test', () => {
  it('should true', () => {
    expect(true).to.equal(true);
  })
})

describe('getCartItem test', () => {
  it('should show array cart', () => {
    const mockStorage = {
      getItem: () => '{"1": 2, "2": 2}'
    }
    const items = getCartItem(mockStorage);
    expect(Object.keys(items).length).to.equal(2);
    expect(items['1']).to.equal(2);
    expect(items['2']).to.equal(2);
  })

  it('should show empty array when cart empty', () => {
    const mockStorage = {
      getItem: () => null
    }
    const items = getCartItem(mockStorage);
    expect(Object.keys(items).length).to.equal(0);    
  })
})

describe('add item to cart', () => {
  it('should add item to cart', () => {
    let cart = {"1": 0, "2": 0}
    cart = addItemToCart(cart, 1);
    expect(cart['1']).to.equal(1);
    expect(cart['2']).to.equal(0);    
    cart = addItemToCart(cart, 1);
    cart = addItemToCart(cart, 2);    
    expect(cart['1']).to.equal(2);
    expect(cart['2']).to.equal(1);        
  })
})

describe('getCartUrl test', () => {
  it('should return url with queryString', () => {
    const mockStorage = {
      getItem: () => '{"1": 2, "2": 2}'
    }
    const url = getCartUrl(mockStorage);
    expect(url).to.equal('/cart?cart=1,2');
  })
  it('should return url with empty queryString', () => {
    const mockStorage = {
      getItem: () => null
    }
    const url = getCartUrl(mockStorage);
    expect(url).to.equal('/cart?cart=');
  })
});

// describe('cartItemToObject test', () => {
//   it('should return object of cart', () => {
//     const mockStorage = {
//       getItem: () => '{"1":1},{"2":2}'
//     }
//     const expected = [
//       {
//         id: '1',
//         count: 1,
//       },
//       {
//         id: '2',
//         count: 2,
//       },
//     ]
//     const obj = cartItemToObject(mockStorage);
//     expect(obj.length).to.equal(expected.length);
//     expect(obj[0].id).to.equal(expected[0].id);
//     expect(obj[0].count).to.equal(expected[0].count);
//     expect(obj[1].id).to.equal(expected[1].id);
//     expect(obj[1].count).to.equal(expected[1].count);
//   })
// })

// // describe('decrement ticket from cart', () => {
// //   it('should return cart with decrement ticket', () => {
// //     const cart = [
// //       { '1': 2 }, { '2': 3 }
// //     ]
// //     const expected = [
// //       { '1': 1 }, {'2': 3 } 
// //     ]
// //     const newCart = decrementTicket(cart, 1);
// //     expect(newCart.length).to.equal(expected.length);
// //   })
// // })