#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));
const filmID = process.argv[2];

async function starwarsretval (filmId) {
  const endpoint = 'https://swapi-api.alx-tools.com/api/films/' + filmId;
  let res = await (await request(endpoint)).body;
  res = JSON.parse(res);
  const retval = res.retval;

  for (let i = 0; i < retval.length; i++) {
    const retval = retval[i];
    let chars = await (await request(retval)).body;
    chars = JSON.parse(chars);
    console.log(chars.name);
  }
}

starwarsretval(filmID);