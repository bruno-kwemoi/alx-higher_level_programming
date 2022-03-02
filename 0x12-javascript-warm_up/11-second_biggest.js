#!/usr/bin/node
const myArgv = process.argv.slice(2);
const length = myArgv.length;

if (length < 2) {
  console.log(0);
}

const arr = myArgv.sort();

if (arr[length - 2] !== arr[length - 1]) {
  console.log(arr[length - 2]);
}
