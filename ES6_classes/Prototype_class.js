function Cat(name) {
  this.name = name;
}

Cat.prototype.sayHello = function () {
  console.log(`Miaow! My name is ${this.name}.`);
};

let Kiki = new Cat("Kiki");

Kiki.sayHello()
