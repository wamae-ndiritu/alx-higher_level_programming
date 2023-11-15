#!/usr/bin/node

const fs = require('fs');
const process = require('process');

const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;

const fileAText = fs.readFileSync(sourceFile1, 'utf-8');
const fileBText = fs.readFileSync(sourceFile2, 'utf-8');

const newText = fileAText + fileBText;

fs.writeFileSync(destinationFile, newText);
