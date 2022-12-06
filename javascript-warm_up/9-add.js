#!/usr/bin/node

const argv = process.argv;

function add (a, b) {
  return a + b;
}

if (argv.length === 4) {
  console.log(add(+argv[2], +argv[3]));
} else {
  console.log(NaN);
}
