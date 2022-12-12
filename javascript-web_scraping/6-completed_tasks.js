#!/usr/bin/node

const argv = process.argv;
const request = require('request');

request(argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const dicty = {};
  for (let i = 0; i < JSON.parse(body).length; i++) {
    if (JSON.parse(body)[i].completed === true) {
      if (JSON.parse(body)[i].userId in dicty) {
        dicty[JSON.parse(body)[i].userId] += 1;
      } else {
        dicty[JSON.parse(body)[i].userId] = 1;
      }
    }
  }
  console.log(dicty);
});
