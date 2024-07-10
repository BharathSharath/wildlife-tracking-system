import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './pages/Home';
import Species from './pages/Species';
import Animals from './pages/Animals';
import Tracking from './pages/Tracking';
import HealthRecords from './pages/HealthRecords';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/species" component={Species} />
        <Route path="/animals" component={Animals} />
        <Route path="/tracking" component={Tracking} />
        <Route path="/health-records" component={HealthRecords} />
      </Switch>
    </Router>
  );
}

export default App;
