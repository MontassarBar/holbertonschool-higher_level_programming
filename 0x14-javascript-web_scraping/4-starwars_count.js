#!/usr/bin/node
const axios = require('axios').default;
let i = 0;
axios.get('https://swapi-api.hbtn.io/api/films')
  .then(function (response) {
    for (let x = 0; x < response.data.results.length; x++) {
      for (let y = 0; y < response.data.results[x].characters.length; y++) {
        if (response.data.results[x].characters[y] === 'https://swapi-api.hbtn.io/api/people/18/') { i++; }
      }
    }
    console.log(i);
  })
  .catch(function (error) {
    console.log(error);
  });
