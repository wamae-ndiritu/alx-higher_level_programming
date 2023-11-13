#!/usr/bin/node
const process = require('process');

const arg = process.argv[2];
const intVal = parseInt(arg);

if (!isNaN(intVal)) {
  console.log(`My number: ${intVal}`);
} else {
  console.log('Not a number');
}
