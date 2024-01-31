# JavaScript Data Manipulation

## 1. How to Use map, filter, and reduce on Arrays

### `map()`

The `map()` method is used to transform each element of an array based on a provided function.

```javascript
const numbers = [1, 2, 3];
const squaredNumbers = numbers.map(num => num * num);
console.log(squaredNumbers); // [1, 4, 9]
```
### `filter()`
The `filter()` method is used to create a new array with elements that satisfy a provided condition.

```javascript
const numbers = [1, 2, 3, 4, 5];
const evenNumbers = numbers.filter(num => num % 2 === 0);
console.log(evenNumbers); // [2, 4]
```
### `reduce()`
The `reduce()` method is used to reduce an array to a single value by applying a function cumulatively to the elements.

```javascript
const numbers = [1, 2, 3, 4, 5];
const sum = numbers.reduce((accumulator, current) => accumulator + current, 0);
console.log(sum); // 15
```

## 2. Typed Arrays
Typed Arrays in JavaScript provide a way to work with binary data in a more efficient and structured manner.

### Examples:
`Int8Array`, `Uint8Array`, `Uint8ClampedArray`, `Int16Array`, `Uint16Array`, `Int32Array`, `Uint32Array`, `Float32Array`, `Float64Array`.
```javascript
const int8Array = new Int8Array([1, 2, 3]);
const uint8Array = new Uint8Array([4, 5, 6]);
const uint8ClampedArray = new Uint8ClampedArray([300, 200, 100]);

console.log(int8Array);        // Int8Array [ 1, 2, 3 ]
console.log(uint8Array);       // Uint8Array [ 4, 5, 6 ]
console.log(uint8ClampedArray); // Uint8ClampedArray [ 255, 200, 100 ]
```

## 3. Set, Map, and WeakLink Data Structures
### `Set`
The `Set` object allows storing unique values and provides methods for manipulation.

```javascript
const mySet = new Set();
mySet.add(1);
mySet.add(2);
mySet.add(3);

console.log(mySet); // Set { 1, 2, 3 }
```

### `Map`
The `Map` object allows storing key-value pairs and provides methods for manipulation.

```javascript
const myMap = new Map();
myMap.set('a', 1);
myMap.set('b', 2);
myMap.set('c', 3);

console.log(myMap); // Map { 'a' => 1, 'b' => 2, 'c' => 3 }
```

### `WeakLink`
The `WeakLink` object provides a collection of objects without preventing them from being garbage-collected.
