#!/usr/bin/node
function factorial (num) {
  if (num < 0) {
    return -1;
  } else if (num === 0 || num === 1) {
    return 1;
  } else {
    return (num * factorial(num - 1));
  }
}
const process = require('process');
const args = process.argv;
if (isNaN(args[2])) {
  console.log('1');
} else {
  console.log(factorial(args[2]));
}
