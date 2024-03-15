const pokemon = Object.freeze([
    { "id": 1, "name": "Bulbasaur", "types": ["poison", "grass"] },
    { "id": 5, "name": "Charmeleon", "types": ["fire"] },
    { "id": 9, "name": "Blastoise", "types": ["water"] },
    { "id": 12, "name": "Butterfree", "types": ["bug", "flying"] },
    { "id": 16, "name": "Pidgey", "types": ["normal", "flying"] },
    { "id": 23, "name": "Ekans", "types": ["poison"] },
    { "id": 24, "name": "Arbok", "types": ["poison"] },
    { "id": 25, "name": "Pikachu", "types": ["electric"] },
    { "id": 35, "name": "Clefairy", "types": ["normal"] },
    { "id": 37, "name": "Vulpix", "types": ["fire"] },
    { "id": 52, "name": "Meowth", "types": ["normal"] },
    { "id": 63, "name": "Abra", "types": ["psychic"] },
    { "id": 67, "name": "Machamp", "types": ["fighting"] },
    { "id": 72, "name": "Tentacool", "types": ["water", "poison"] },
    { "id": 74, "name": "Geodude", "types": ["rock", "ground"] },
    { "id": 87, "name": "Dewgong", "types": ["water", "ice"] },
    { "id": 98, "name": "Krabby", "types": ["water"] },
    { "id": 115, "name": "Kangaskhan", "types": ["normal"] },
    { "id": 122, "name": "Mr. Mime", "types": ["psychic"] },
    { "id": 133, "name": "Eevee", "types": ["normal"] },
    { "id": 144, "name": "Articuno", "types": ["ice", "flying"] },
    { "id": 145, "name": "Zapdos", "types": ["electric", "flying"] },
    { "id": 146, "name": "Moltres", "types": ["fire", "flying"] },
    { "id": 148, "name": "Dragonair", "types": ["dragon"] }
]);


const pokemonDivisibleBy3 = pokemon.filter(p => p.id % 3 === 0);
console.log(pokemonDivisibleBy3);

const firePokemons = pokemon.filter(p => p.types.includes("fire"));
console.log(firePokemons);

const multiTypePokemons = pokemon.filter(p => p.types.length > 1);
console.log(multiTypePokemons);

const pokemonNames = pokemon.map(p => p.name);
console.log(pokemonNames);

const pokemonNamesAndIdsGreaterThan99 = pokemon.filter(p => p.id > 99)
    .map(p => ({ name: p.name, id: p.id }));
console.log(pokemonNamesAndIdsGreaterThan99);

const poisonPokemons = pokemon.filter(p => p.types.includes("poison"))
    .map(p => ({ name: p.name, types: p.types }));
console.log(poisonPokemons);

const pokemonWithSecondFlying = pokemon.filter(p => p.types.length > 1 && p.types[1] === "flying")
    .map(p => ({ name: p.name, firstType: p.types[0] }));
console.log(pokemonWithSecondFlying);

const normalPokemonCount = pokemon.filter(p => p.types.includes("normal")).length;
console.log(normalPokemonCount);

const pokemonExceptId148 = pokemon.filter(p => p.id !== 148);
console.log(pokemonExceptId148);

const modifiedPokemon = pokemon.map(p => {
    if (p.id === 35 && p.types.includes("normal")) {
        const types = p.types.map(type => type === "normal" ? "fairy" : type);
        return { ...p, types };
    }
    return p;
});

console.log(modifiedPokemon);

