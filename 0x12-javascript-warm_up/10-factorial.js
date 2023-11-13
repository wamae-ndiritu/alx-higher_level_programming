#!/usr/bin/node
const process = require('process');

const num = parseInt(process.argv[2]);

function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  }

  return n * factorial(n - 1);
}

const result = factorial(num);
console.log(result);
