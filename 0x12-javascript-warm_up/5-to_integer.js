#!/usr/bin/node
const myArgv = process.argv.slice(2);
const isNumber = parseInt(myArgv[0]);
if (!isNumber) {
  console.log('Not a number');
} else {
  console.log('My number:', isNumber);
}
