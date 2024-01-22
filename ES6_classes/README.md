# Object-Oriented Programming in JavaScript

This repository provides a brief guide on defining classes, adding methods, incorporating static methods, extending classes, and an introduction to metaprogramming using symbols in JavaScript.

## Table of Contents

1. [Defining a Class](#defining-a-class)
2. [Adding Methods to a Class](#adding-methods-to-a-class)
3. [Adding a Static Method to a Class](#adding-a-static-method-to-a-class)
4. [Extending a Class](#extending-a-class)
5. [Metaprogramming and Symbols](#metaprogramming-and-symbols)

## 1. Defining a Class

In JavaScript, a class is a blueprint for creating objects. It encapsulates data and behavior into a single unit. To define a class, use the `class` keyword:

```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }
}
```

## 2. Adding Methods to a Class
Methods are functions associated with an object. You can add methods to a class by defining functions within the class:
```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    console.log(`${this.name} makes a sound.`);
  }
}
```
## 3. Adding a Static Method to a Class
Static methods are called on the class itself, not on instances of the class. They are defined using the **'static'** keyword:
```javascript
class MathUtils {
  static add(x, y) {
    return x + y;
  }
}

// Usage
const sum = MathUtils.add(5, 3);
console.log(sum); // Output: 8
```
## 4. Extending a Class
Inheritance in JavaScript is achieved by using the **'extends'** keyword to create a subclass. The subclass inherits properties and methods from the superclass:
```javascript
class Bird extends Animal {
  fly() {
    console.log(`${this.name} can fly.`);
  }
}
```
## 5. Metaprogramming and Symbols
Metaprogramming involves writing code that manipulates the structure or behavior of the program itself. Symbols in JavaScript are a unique data type that can be used for metaprogramming:
```javascript
const key = Symbol('description');
const obj = {
  [key]: 'value'
};

console.log(obj[key]); // Output: value
```
Feel free to explore each section for a detailed understanding of the concepts. Happy coding!
