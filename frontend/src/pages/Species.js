import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Species() {
  const [species, setSpecies] = useState([]);

  useEffect(() => {
    axios.get('/api/species')
      .then(response => setSpecies(response.data))
      .catch(error => console.error('There was an error fetching the species data!', error));
  }, []);

  return (
    <div>
      <h1>Species List</h1>
      <ul>
        {species.map(species => (
          <li key={species.species_id}>{species.common_name}</li>
        ))}
      </ul>
    </div>
  );
}

export default Species;
