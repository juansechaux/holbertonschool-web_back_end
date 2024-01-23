export default class Currency {
  constructor(code, name) {
    this._code = '';
    this._name = '';

    this.code = code;
    this.name = name;
  }

  displayFullCurrency() {
    // use template literals. it use inverted quotation marks
    return `${this._name} (${this._code})`; // return this._name + ' (' + this._code + ')'
  }

  get code() {
    return this._code;
  }

  get name() {
    return this._name;
  }

  set code(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this._code = value;
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = value;
  }
}
