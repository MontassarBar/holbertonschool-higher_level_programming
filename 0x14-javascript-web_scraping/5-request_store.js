#!/usr/bin/node
const axios = require('axios').default;
const process = require('process');
const fs = require('fs');
axios.get(process.argv[2])
  .then(function (response) {
    fs.writeFile(process.argv[3], response.data, (err) => {
      if (err) throw err;
    });
  });
