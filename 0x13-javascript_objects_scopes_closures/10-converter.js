#!/usr/bin/node
exports.converter = function (base) {
  function converter (x) {
    return parseInt(x).toString(base);
  }
  return converter;
};
