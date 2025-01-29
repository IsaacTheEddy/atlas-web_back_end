// const custoumIterable = {
//   [Symbol.iterator]() {
//     let counter = 0;
//     return {
//       next() {
//         if (counter < 5) {
//           counter++;
//           return { done: false, value: counter };
//         } else {
//           return { done: true, value: undefined };
//         }
//       }
//     }
//   }
// }


// for (const x of custoumIterable) {
//   console.log((custoumIterable));
// }

// Symbol();
// console.log(Symbol());

// console.log(Symbol('foo'));
// console.assert(Symbol('foo').toString() === 'Symbol(foo)')

var myObj = {};
var fooSym = Symbol('foo');
var otherSym = Symbol('bar');
myObj['foo'] = 'bar';
myObj[fooSym] = 'baz';
console.log(Object.entries(myObj));
console.log(Object.getOwnPropertyNames(myObj));
console.log(Object.getOwnPropertySymbols(myObj));
console.assert(Object.getOwnPropertySymbols(myObj)[0] === fooSym);
