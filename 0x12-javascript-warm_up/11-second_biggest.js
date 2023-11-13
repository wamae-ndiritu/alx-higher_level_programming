#!/usr/bin/node
const process = require('process');

const args = process.argv.slice(2);

const integers = args.map(Number);

const sortedInts = integers.sort((a, b) => b - a);

if (sortedInts.length < 2) {
  if (sortedInts.length === 1) {
    console.log(1);
  } else {
    console.log(0);
  }
} else {
  console.log(sortedInts[1]);
}
