export default class HolbertonClass {
  constructor(size, location) {
    if (typeof size !== 'number' || size <= 0) {
      throw new Error('Size must be a positive, non-zero number');
    }

    if (typeof location !== 'string' || location.length <= 0) {
      throw new Error('Location must be a non-empty string');
    }

    this._size = size;
    this._location = location;
  }

  get size() {
    return this._size;
  }

  set size(value) {
    if (typeof value !== 'number' || value <= 0) {
      throw new Error('Size must be a non-zero number');
    }
    this._size = value;
  }

  get location() {
    return this._location;
  }

  set location(value) {
    if (typeof value !== 'string' || value.length <= 0) {
      throw new Error('Location must be a non empty string');
    }
    this._location = value;
  }

  [Symbol.toPrimitive](type) {
    if (type === 'string') {
      return this._location;
    }
    if (type === 'number') {
      return this._size;
    }
    if (type === 'undefined') {
      throw new Error('Type must be a valid number or string');
    }
    return null;
  }
}
