#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && w !== undefined && h !== undefined) {
      // values are neither 0 nor negative nor undefined
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
