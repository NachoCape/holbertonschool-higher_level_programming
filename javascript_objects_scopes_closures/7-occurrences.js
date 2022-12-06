#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let res = 0;
  list.forEach(element => {
    if (searchElement === element) {
      res += 1;
    }
  });
  return res;
};
