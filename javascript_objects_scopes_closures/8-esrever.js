#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.lenght;
  console.log(len);
  let j = len;
  for (let i = 0; i < len / 2; i++) {
    const aux = list[i];
    list[i] = list[j];
    console.log(list[i]);
    list[j] = aux;
    j--;
  }
};
