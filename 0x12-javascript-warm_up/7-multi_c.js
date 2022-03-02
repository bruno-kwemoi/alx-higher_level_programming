#!/usr/bin/node
const myArgv = process.argv.slice(2);
const isNumber = parseInt(myArgv[0]);

if (!isNumber) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < isNumber; i++) {
    console.log('C is fun');
  }
}
