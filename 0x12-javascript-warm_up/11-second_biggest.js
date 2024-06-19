#!/usr/bin/node
const args = process.argv;
const len = args.length;
let i, first, second;

first = second = 0;
for (i = 2; i < len; i++)
{
  if (args[i] > first) {
    second = first;
    first = args[i];
  } else if (args[i] != first && args[i] > second) {
    second = args[i];
  }
}

console.log(second);
