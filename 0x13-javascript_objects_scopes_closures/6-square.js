#!/usr/bin/node
const GreaterSquare = require('./5-square.js');

class Square extends GreaterSquare {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        console.log('C'.repeat(this.height));
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
