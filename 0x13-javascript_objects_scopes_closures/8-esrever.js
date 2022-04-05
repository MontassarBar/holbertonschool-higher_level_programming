#!/usr/bin/node
exports.esrever = function (list) {
  let x = list.length - 1;
  let y = 0;
  const ll = [];
  while (x >= 0) {
    ll[y] = list[x];
    x--;
    y++;
  }
  return ll;
};
