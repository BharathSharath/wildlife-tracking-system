import React, { useState, useEffect } from 'react';
import axios from 'axios';

function HealthRecords() {
  const [healthRecords, setHealthRecords] = useState([]);

  useEffect(() => {
    axios.get('/api/health_records')
      .then(response => setHealthRecords(response.data))
      .catch(error => console.error('There was an error fetching the health records data!', error));
  }, []);

  return (
    <div>
      <h1>Health Records</h1>
      <ul>
        {healthRecords.map(record => (
          <li key={record.record_id}>{record.checkup_date}: {record.health_status}</li>
        ))}
      </ul>
    </div>
  );
}

export default HealthRecords;
