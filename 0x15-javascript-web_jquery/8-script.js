$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (let x = 0; x < data.results.length; x++) { $('UL#list_movies').append($('<li></li>').text(data.results[x].title)); }
});
