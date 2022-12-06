#!/usr/bin/node

const argv = process.argv;

if (argv.length === 2) {
  console.log('Missing number of occurrences');
} else if (isNaN(argv[2])) {
  console.log('');
} else {
  for (let i = 0; i < argv[2]; i++) {
    console.log('C is fun');
  }
}
