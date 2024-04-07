
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Pokemon = props =>{
    const [responseData, setResponseData] = useState(null);
    useEffect(()=>{
        axios.get('https://pokeapi.co/api/v2/pokemon?limit=151&offset=0')
            .then(response=>{setResponseData(response.data)})
    }, []);


    const capitalizeFirstLetter = (string) => {
        return string.charAt(0).toUpperCase() + string.slice(1);
    };
    
    return (
        <div className='container'>
            <div className='title'><h1>Pokemon API</h1></div>
            <div style={{ display: 'flex', justifyContent: 'center' }}> {/* Centering the list */}
                <ul style={{ paddingLeft: 0, textAlign: 'center' }}> {/* Adjusting the padding of the ul element */}
                    {responseData && responseData.results && responseData.results.map((pokemon, index) => (
                        <li key={index} style={{ listStyle: 'circle' }}>
                            {capitalizeFirstLetter(pokemon.name)}
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
}
    


export default Pokemon