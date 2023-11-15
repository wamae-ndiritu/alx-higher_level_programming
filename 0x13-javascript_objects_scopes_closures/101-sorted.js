#!/usr/bin/node

const dict = require('./101-data').dict;

const sortedDict = {};

for (const [key, value] of Object.entries(dict)) {
  if (!sortedDict[value]) {
    sortedDict[value] = [];
  }

  sortedDict[value].push(key);
}
console.log(dict);
console.log(sortedDict);
