#!/usr/bin/node

const argv = process.argv;
const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/' + argv[2], function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body).title);
});
