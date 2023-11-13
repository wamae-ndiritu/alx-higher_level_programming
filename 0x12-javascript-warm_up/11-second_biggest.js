#!/usr/bin/node
const process = require('process');

const argumentsCount = process.argv.length;
const intList = [];
for (let i = 2; i < argumentsCount; i++) {
  intList.push(parseInt(process.argv[i]));
}

intList.sort();

if (argumentsCount - 2 === 0) {
  console.log(0);
} else {
  const secondBiggest = intList[argumentsCount - 4];
  console.log(secondBiggest);
}
