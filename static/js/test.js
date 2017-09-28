import { expect } from 'chai';
import {
  getCartItem,
  getCartUrl,
} from './script-test';

describe('simple test', () => {
  it('should true', () => {
    expect(true).to.equal(true);
  })
})

describe('getCartItem test', () => {
  it('should show array cart', () => {
    const mockStorage = {
      getItem: () => '1,2,3'
    }
    const items = getCartItem(mockStorage);
    expect(items.length).to.equal(3);
    expect(items[0]).to.equal('1');
    expect(items[1]).to.equal('2');
    expect(items[2]).to.equal('3');
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
      getItem: () => '1,2,3'
    }
    const url = getCartUrl(mockStorage);
    expect(url).to.equal('/cart?cart=1,2,3');
  })
  it('should return url with empty queryString', () => {
    const mockStorage = {
      getItem: () => undefined
    }
    const url = getCartUrl(mockStorage);
    expect(url).to.equal('/cart?cart=');
  })
});
