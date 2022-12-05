#!/usr/bin/node

import { argv } from 'process';

if (isNaN(argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argv[2]);
}
