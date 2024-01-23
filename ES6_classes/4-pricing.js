import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = 0;
    this._currency = '';

    this.amount = amount;
    this.currency = currency;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency._name} (${this._currency._code})`;
  }

  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number' || typeof conversionRate !== 'number') {
      throw new TypeError('Both amount and conversionRate must be numbers');
    }
    return amount * conversionRate;
  }

  get amount() {
    return this._amount;
  }

  get currency() {
    return this._currency;
  }

  set amount(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Amount must be a Number');
    }
    this._amount = value;
  }

  set currency(value) {
    if (value instanceof Currency) {
      this._currency = value;
    } else {
      throw new TypeError('Currency is not instance of Currency');
    }
  }
}
