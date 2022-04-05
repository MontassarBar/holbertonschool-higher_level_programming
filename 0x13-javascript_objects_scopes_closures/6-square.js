#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let Rect = '';
    let x = 0;
    let y = 0;
    while (x < this.width) {
      Rect += c;
      x++;
    }
    while (y < this.height) {
      console.log(Rect);
      y++;
    }
  }
}
module.exports = Square;
