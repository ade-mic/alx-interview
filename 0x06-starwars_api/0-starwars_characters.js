const axios = require('axios').default;

async function getStarWars(movieId) {
    try {
        const api = `http://swapi.dev/api/films/${movieId}`
        const response = await axios.get(api);
        const movieData = response.data;
        const characterUrls = movieData.characters;

        for (const url of characterUrls) {
            const charResponse = await axios.get(url);
            console.log(charResponse.data.name)
        } 
    } catch (error) {
        console.log(`Error: Unable to fetch data for movie ID ${movieId}`);
    }
}

const movieId  = process.argv[2];
if (!movieId) {
    console.log("Usage: node script.js <movie_id>");
} else {
    getStarWars(movieId)
}
