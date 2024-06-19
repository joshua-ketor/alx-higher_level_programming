#!/usr/bin/node
const noOfArg = process.argv.length;

if (noOfArg === 2) {
  console.log('No argument');
} else if (noOfArg === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
