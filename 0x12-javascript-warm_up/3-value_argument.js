#!/usr/bin/node
const noOfArg = process.argv;

if (noOfArg[2] === undefined) {
  console.log('No argument');
} else {
  console.log(noOfArg[2]);
}
