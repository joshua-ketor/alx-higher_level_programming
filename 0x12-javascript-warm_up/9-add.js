#!/usr/bin/node
const args = process.argv;
const arg1 = Number(args[2]);
const arg2 = Number(args[3]);

function add (a, b) {
  console.log(a + b);
}

add(arg1, arg2);
