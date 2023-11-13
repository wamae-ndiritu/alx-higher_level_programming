#!/usr/bin/node
const process = require('process');

const firstInt = parseInt(process.argv[2]);
const secondInt = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

const sum = add(firstInt, secondInt);
console.log(sum);
