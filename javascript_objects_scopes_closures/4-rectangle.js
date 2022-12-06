#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str = '';
    for (let i = 0; i < this.width; i++) {
      str = str + 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(str);
    }
  }

  rotate () {
    const aux = this.height;
    this.height = this.width;
    this.width = aux;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
