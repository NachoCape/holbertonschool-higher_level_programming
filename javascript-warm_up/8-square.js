#!/usr/bin/node

const argv = process.argv;

if (argv.length === 2) {
  console.log('Missing size');
} else if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  let str = '';
  for (let i = 0; i < argv[2]; i++) {
    str = str + 'X';
  }
  for (let j = 0; j < argv[2]; j++) {
    console.log(str);
  }
}
