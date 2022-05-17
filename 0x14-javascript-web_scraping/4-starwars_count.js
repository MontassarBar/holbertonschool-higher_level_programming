#!/usr/bin/node
const axios = require('axios').default;
const process = require('process');
let i = 0;
axios.get(process.argv[2])
  .then(function (response) {
    for (let x = 0; x < response.data.results.length; x++) {
      for (let y = 0; y < response.data.results[x].characters.length; y++) {
        axios.get(response.data.results[x].characters[y])
          .then(function (re) {
            if (re.data.name === 'Wedge Antilles') { i++; }
          });
      }
    }
    console.log(i);
  })
  .catch(function (error) {
    console.log(error);
  });
