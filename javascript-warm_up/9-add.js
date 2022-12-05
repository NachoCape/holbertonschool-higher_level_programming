#!/usr/bin/node

import { argv } from 'process';

function add (a, b) {
  return a + b;
}

if (argv.length === 4) {
  console.log(add(+argv[2], +argv[3]));
}
