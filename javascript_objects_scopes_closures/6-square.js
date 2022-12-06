#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let str = '';
    for (let i = 0; i < this.height; i++) {
      str = str + c;
    }
    for (let j = 0; j < this.width; j++) {
      console.log(str);
    }
  }
};
