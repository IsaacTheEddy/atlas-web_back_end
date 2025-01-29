export default class Airport {
  constructor(name, code) {
    if (typeof name !== 'string' || name.length <= 0) {
      throw new Error('Name must be a non-empty string');
    }
    if (typeof code !== 'string' || code.length <= 0) {
      throw new Error('Code must be a non-empty string');
    }

    this._name = name;
    this._code = code;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string' || value.length <= 0) {
      throw new Error('Name must be a non-empty string');
    }
    this._name = value;
  }

  get code() {
    return this._code;
  }

  set code(value) {
    if (typeof value !== 'string' || value.length <= 0) {
      throw new Error('Code must be a non-empty string');
    }
    this._code = value;
  }

  get [Symbol.toStringTag]() {
    return `${this._code}`;
  }
}
