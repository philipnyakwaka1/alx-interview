#!/usr/bin/node

const https = require('https')
function fetchAPI(url) {
    return new Promise((resolve, reject) => {
        https.get(url, (resp) => {
            let data = '';
            resp.on('data', (chunk) => {
                data += chunk;
            });

            resp.on('end', () => {
                try {
                    const parsedData = JSON.parse(data);
                    resolve(parsedData);
                } catch (error) {
                    reject('Failed to parse data');
                }
            });
        }).on('error', (error) => {
            reject(`Error: ${error}`);
        });
    });
}


async function getCharacter() {
    try {
        const resp = await fetchAPI(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`);
        const characters = resp.characters;
        for (let i = 0; i < characters.length; i++)
        {
            const character = await fetchAPI(characters[i]);
            console.log(character.name);
        }
    } catch(err) {
        console.log(`error: ${err}`);
    }
}
getCharacter();

