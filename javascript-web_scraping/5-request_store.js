#!/usr/bin/node

const argv = process.argv;
const request = require('request');
const fs = require('fs');

request(argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(argv[3], body, 'utf-8', function (er) {
    if (er) {
      console.log(er);
    }
  });
});
