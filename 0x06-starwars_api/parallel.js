#!/usr/bin/node

const axios = require('axios')

async function fetchCharacter(url) {
    try {
        resp = await axios.get('https://swapi-api.alx-tools.com/api/people/1/')
        console.log(resp.data)
    } catch(err) {
        console.log(err)
    }
}
fetchCharacter()