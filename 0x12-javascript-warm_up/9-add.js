#!/usr/bin/node
function add (a, b) {
  const x = a + b;
  return x;
}
const { argv } = require('process');
const process = require('process');
const args = process.argv;
const y = add(parseInt(args[2]), parseInt(args[3]));
if (isNaN(argv[2]) || isNaN(argv[3])) {
  console.log('NaN');
} else {
  console.log(y);
}
