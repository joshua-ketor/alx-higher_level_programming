#!/usr/bin/node
const GreaterSquare = require('./5-square.js');

class Square extends GreaterSquare {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.size; i++) {
        console.log('C'.repeat(this.size));
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
