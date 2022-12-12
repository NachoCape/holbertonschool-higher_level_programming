#!/usr/bin/node

// const argv = process.argv;
const { argv } = require('process');
const request = require('request');

request(argv[2], function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  const wedgeAntilles = 'https://swapi-api.alx-tools.com/api/people/18/';
  let count = 0;
  for (let i = 0; i < JSON.parse(body).results.length; i++) {
    for (let j = 0; j < JSON.parse(body).results[i].characters.length; j++) {
      if (JSON.parse(body).results[i].characters[j] === wedgeAntilles) {
        count += 1;
      }
    }
  }
  console.log(count);
});
