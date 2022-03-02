#!/usr/bin/node
const myArgv = process.argv.slice(2);
const n = parseInt(myArgv[0]);

function factorial (n) {
  if (!parseInt(myArgv[0])) {
    return (1);
  }
  if (n === 0) {
    return (1);
  }
  return (n * factorial(n - 1));
}

console.log(factorial(n));
