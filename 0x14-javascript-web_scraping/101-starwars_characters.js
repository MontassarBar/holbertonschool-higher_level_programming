#!/usr/bin/node
const axios = require('axios').default;
const process = require('process');
axios.get('https://swapi-api.hbtn.io/api/films/')
  .then(function (response) {
    for (let y = 0; y < response.data.results[process.argv[2] - 1].characters.length; y++) {
      axios.get(response.data.results[process.argv[2] - 1].characters[y])
        .then(function (re) {
          console.log(re.data.name);
        });
    }
  }
  );
