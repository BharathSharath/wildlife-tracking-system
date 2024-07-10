import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Animals() {
  const [animals, setAnimals] = useState([]);

  useEffect(() => {
    axios.get('/api/animals')
      .then(response => setAnimals(response.data))
      .catch(error => console.error('There was an error fetching the animals data!', error));
  }, []);

  return (
    <div>
      <h1>Animals List</h1>
      <ul>
        {animals.map(animal => (
          <li key={animal.animal_id}>{animal.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default Animals;
