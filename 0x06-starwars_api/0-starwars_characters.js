#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    return;
  }

  const film = JSON.parse(body);
  film.characters.forEach(characterUrl => {
    request(characterUrl, (err, resp, charBody) => {
      if (err) {
        console.error(err);
        return;
      }

      if (resp.statusCode !== 200) {
        console.error(`Error: ${resp.statusCode}`);
        return;
      }

      const character = JSON.parse(charBody);
      console.log(character.name);
    });
  });
});
