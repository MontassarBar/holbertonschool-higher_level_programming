#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let x = 0;
  let y = 0;
  while (x < list.length) {
    if (list[x] === searchElement) {
      y++;
    }
    x++;
  }
  return y;
};
