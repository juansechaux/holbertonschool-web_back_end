# ES6 Features Overview

## What is ES6?

ES6, or ECMAScript 2015, is the sixth edition of the ECMAScript standard, which is the scripting language specification that JavaScript is based on. It introduced several new features and enhancements to the language.

## New Features Introduced in ES6

ES6 brought many new features to JavaScript, including:

- **let and const Declarations**
- **Arrow Functions**
- **Template Literals**
- **Destructuring Assignment**
- **Classes**
- **Default Parameters**
- **Rest and Spread Operators**
- **Iterators and for-of Loop**
- **Block-Scoped Declarations**
- **Enhanced Object Literals**
- **Modules**

## Difference Between a Constant and a Variable

In ES6, you use `const` to declare constants and `let` to declare variables. The main difference is that the value of a constant cannot be reassigned after its initial assignment, while a variable's value can be changed.

```javascript
const pi = 3.14159;
let count = 0;
```
## Block-Scoped Variables
Variables declared with let and const are block-scoped, meaning they are only accessible within the block of code where they are defined.

```javascript
if (true) {
  let x = 10;
  const y = 20;
}

console.log(x); // ReferenceError: x is not defined
console.log(y); // ReferenceError: y is not defined
```
## Arrow Functions and Function Parameters Default to Them
Arrow functions provide a concise syntax for writing functions. They do not have their own this and arguments, making them especially useful for callback functions and concise one-liners.

```javascript
const add = (a, b) => a + b;
const greet = name => `Hello, ${name}!`;

```
## Rest and Spread Function Parameters
The rest parameter (...) allows a function to accept an indefinite number of arguments as an array, while the spread operator (...) can be used to spread the elements of an array or object into individual elements.

```javascript
function sum(...numbers) {
  return numbers.reduce((total, num) => total + num, 0);
}

const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const mergedArray = [...arr1, ...arr2];
```

## String Templating in ES6
Template literals provide a more flexible way to concatenate strings by allowing placeholders and expressions inside a string.

```javascript
const name = 'John';
const greeting = `Hello, ${name}!`; // Hello, John!
```
## Object Creation and Their Properties in ES6
ES6 introduced shorthand syntax for creating object literals, computed property names, and method definitions in object literals.

```javascript
const key = 'color';
const value = 'red';

const obj = {
  [key]: value,
  method() {
    // method definition
  }
};
```

## Iterators and for-of Loops
Iterators provide a uniform way to iterate over different data structures. The for-of loop simplifies the iteration process.

```javascript
const iterable = [1, 2, 3];

for (const element of iterable) {
  console.log(element);
}
```
This is a brief overview of some key ES6 features.

## Sources
- [ECMAScript 6 - ECMAScript 2015](https://www.w3schools.com/js/js_es6.asp)
- [Statements and declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements)
- [Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
- [Default parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)
- [Rest parameter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
- [Javascript ES6 — Iterables and Iterators](https://towardsdatascience.com/javascript-es6-iterables-and-iterators-de18b54f4d4)
