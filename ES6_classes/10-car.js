const cloneSymbol = Symbol('cloneCar');

export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  get brand() {
    return this._brand;
  }

  get motor() {
    return this._motor;
  }

  get color() {
    return this._color;
  }

  [cloneSymbol]() {
    // Create a new instance of the same class with the current property values
    const clonedCar = new this.constructor(this._brand, this._motor, this._color);
    return clonedCar;
  }

  cloneCar() {
    return this[cloneSymbol]();
  }
}
