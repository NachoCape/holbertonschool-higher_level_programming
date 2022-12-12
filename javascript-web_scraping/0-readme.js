#!/usr/bin/node

const argv = process.argv;

const fs = require('fs');
// console.log(argv[2]);
fs.readFile(argv[2], 'utf-8', function (err, data) {
  if (err) {
    return;
  }
  console.log(data);
});
