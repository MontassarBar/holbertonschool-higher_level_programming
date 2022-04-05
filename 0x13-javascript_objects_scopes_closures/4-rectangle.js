#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let Rect = '';
    let x = 0;
    let y = 0;
    while (x < this.width) {
      Rect += 'X';
      x++;
    }
    while (y < this.height) {
      console.log(Rect);
      y++;
    }
  }

  rotate () {
    const i = this.width;
    this.width = this.height;
    this.height = i;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}
module.exports = Rectangle;
