#!/usr/bin/node

exports.esrever = function (list) {
  const len = Object.keys(list).length;
  let j = len - 1;
  for (let i = 0; i < len / 2; i++) {
    const aux = list[i];
    list[i] = list[j];
    list[j] = aux;
    j--;
  }
  return list;
};
