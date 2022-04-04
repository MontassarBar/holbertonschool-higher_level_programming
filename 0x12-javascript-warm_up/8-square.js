#!/usr/bin/node
const process = require('process');
const args = process.argv[2];
let x = 0;
let y = 0;
let square = '';
if (isNaN(args)) {
  console.log('Missing size');
}
while (y < args) {
  square += 'X';
  y++;
}
while (x < args) {
  console.log(square);
  x++;
}
