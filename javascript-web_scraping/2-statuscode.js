#!/usr/bin/node

const argv = process.argv;
const url = require('https');

url.get(argv[2], function (res) {
  console.log('code: ' + res.statusCode);
});
