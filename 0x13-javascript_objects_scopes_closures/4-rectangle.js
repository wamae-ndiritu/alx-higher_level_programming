#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && w !== undefined && h !== undefined) {
      // values are neither 0 nor negative nor undefined
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width !== undefined || this.height !== undefined) {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += 'X';
        }
        console.log(row);
      }
    }
  }

  rotate () {
    const tempHeight = this.height;
    this.height = this.width;
    this.width = tempHeight;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
