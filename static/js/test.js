import { expect } from 'chai';
import {
  getCartItem,
  getCartUrl,
  cartItemToObject,
} from './script-test';

describe('simple test', () => {
  it('should true', () => {
    expect(true).to.equal(true);
  })
})

describe('getCartItem test', () => {
  it('should show array cart', () => {
    const mockStorage = {
      getItem: () => '{"1":1},{"2":2}'
    }
    const items = getCartItem(mockStorage);
    expect(items.length).to.equal(2);
    expect(items[0]['1']).to.equal(1);
    expect(items[1]['2']).to.equal(2);
  })
  it('should show empty array when cart empty', () => {
    const mockStorage = {
      getItem: () => undefined
    }
    const items = getCartItem(mockStorage);
    expect(items.length).to.equal(0);
  })
})

describe('getCartUrl test', () => {
  it('should return url with queryString', () => {
    const mockStorage = {
      getItem: () => '{"1":1},{"2":2}'
    }
    const url = getCartUrl(mockStorage);
    expect(url).to.equal('/cart?cart=1,2');
  })
  it('should return url with empty queryString', () => {
    const mockStorage = {
      getItem: () => undefined
    }
    const url = getCartUrl(mockStorage);
    expect(url).to.equal('/cart?cart=');
  })
});

describe('cartItemToObject test', () => {
  it('should return object of cart', () => {
    const mockStorage = {
      getItem: () => '{"1":1},{"2":2}'
    }
    const expected = [
      {
        id: '1',
        count: 1,
      },
      {
        id: '2',
        count: 2,
      },
    ]
    const obj = cartItemToObject(mockStorage);
    expect(obj.length).to.equal(expected.length);
    expect(obj[0].id).to.equal(expected[0].id);
    expect(obj[0].count).to.equal(expected[0].count);
    expect(obj[1].id).to.equal(expected[1].id);
    expect(obj[1].count).to.equal(expected[1].count);
  })
})
