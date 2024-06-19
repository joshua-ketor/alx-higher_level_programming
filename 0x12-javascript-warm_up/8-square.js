#!/usr/bin/node
const size = Number(process.argv[2]);
let i;

if (!size) {
  console.log('Missing size');
} else {
  for (i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
