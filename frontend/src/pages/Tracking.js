import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Tracking() {
  const [trackingData, setTrackingData] = useState([]);

  useEffect(() => {
    axios.get('/api/tracking')
      .then(response => setTrackingData(response.data))
      .catch(error => console.error('There was an error fetching the tracking data!', error));
  }, []);

  return (
    <div>
      <h1>Tracking Data</h1>
      <ul>
        {trackingData.map(track => (
          <li key={track.tracking_id}>{track.timestamp}: {track.latitude}, {track.longitude}</li>
        ))}
      </ul>
    </div>
  );
}

export default Tracking;
