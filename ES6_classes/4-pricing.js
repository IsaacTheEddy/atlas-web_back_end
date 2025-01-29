import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;

    if (!(currency instanceof Currency)) {
      throw new Error('Must be an instance of currency');
    }
    this._currency = currency;

    Object.defineProperty(this, 'amount', {
      get: () => this._amount,
      set: (value) => {
        if (typeof value === 'number') {
          this._amount = value;
        } else {
          throw new Error('Amount must be a number');
        }
      },
    });

    Object.defineProperty(this, 'currency', {
      get: () => this._currency,
      set: (value) => {
        if (value instanceof Currency) {
          this._currency = value;
        } else {
          throw new Error('Must be an instance of currency');
        }
      },
    });
  }

  displayFullPrice() {
    return (`${this.amount} ${this.currency.name} (${this.currency.code})`);
  }

  static convertPrice(conversionRate, amount) {
    if (typeof conversionRate === 'number' && conversionRate > 0) {
      return ((conversionRate * 100) * amount) / 100;
    }
    throw new Error('Conversion rate must be a positive number');
  }
}
