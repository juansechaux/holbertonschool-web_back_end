export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  get size() {
    return this._size;
  }

  get location() {
    return this._location;
  }

  [Symbol.toPrimitive](hint) {
    if (hint === 'number') {
      return this._size;
    } /* eslint-disable no-else-return */ else if (hint === 'string') {
      return this._location;
    } else {
      throw new TypeError('Value not find');
    }
  }
}
