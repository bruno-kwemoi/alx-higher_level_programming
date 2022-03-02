#!/usr/bin/node
const myArgv = process.argv.slice(2);
function add(a, b)
{
    let sum = parseInt(a) + parseInt(b);
    return sum;
}

let result = add(myArgv[0], myArgv[1]);
console.log(result);
