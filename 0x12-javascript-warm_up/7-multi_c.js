#!/usr/bin/node
const process = require('process');
const args = process.argv[2];
let x = 0;
if (isNaN(args)) {
  console.log('Missing number of occurrences');
}
while (x < args) {
  console.log('C is fun');
  x++;
}
