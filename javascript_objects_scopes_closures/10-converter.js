#!/usr/bin/node

exports.converter = function (base) {
  return function (num) { /* declare this function because otherwise get 'TypeError: myConverter is not a function' */
    return num.toString(base);
  };
};
