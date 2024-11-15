#!/usr/bin/node
const request = require('request');

const makeRequest = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

async function getAndPrintCharacters () {
  if (process.argv.length !== 3) {
    console.error('Please provide a movie ID');
    process.exit(1);
  }

  const movieId = process.argv[2];
  const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

  try {
    const filmData = await makeRequest(filmUrl);
    const characters = filmData.characters;

    for (const characterUrl of characters) {
      try {
        const character = await makeRequest(characterUrl);
        console.log(character.name);
      } catch (error) {
        console.error(`Error fetching character: ${error.message}`);
      }
    }
  } catch (error) {
    console.error(`Error fetching movie data: ${error.message}`);
    process.exit(1);
  }
}

getAndPrintCharacters();
