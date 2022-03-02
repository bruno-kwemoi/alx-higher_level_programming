#!/usr/bin/node
const myArgv = process.argv.slice(2);
const isNumber = parseInt(myArgv[0]);
const square = 'X';

if (!isNumber) {
  console.log('Missing size');
} else {
  for (let i = 0; i < isNumber; i++) {
    console.log(square.repeat(isNumber));
  }
}
