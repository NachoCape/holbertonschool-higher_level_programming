#!/usr/bin/node

import { argv } from 'process';

if (argv.length <= 3) {
  console.log(0);
} else {
  let max = argv[2];
  let res = argv[2];
  for (let i = 3; argv[i]; i++) {
    if (+argv[i] > +max) {
      max = argv[i];
    }
  }
  for (let j = 3; argv[j]; j++) {
    if (+argv[j] < +max && +argv[j] > +res) {
      res = +argv[j];
    } else if (+res === +max && +argv[j] < +res) {
      res = +argv[j];
    }
  }
  console.log(res);
}
