#!/usr/bin/node

import { argv } from 'process';

function recu (num) {
  if (num > 0) {
    return num * recu(num - 1);
  } else {
    return 1;
  }
}
if (argv.length === 3) {
  console.log(recu(argv[2]));
} else {
  console.log(NaN);
}
