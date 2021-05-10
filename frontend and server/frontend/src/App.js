//import logo from './logo.svg';
import './App.css';
import Nav from './components/Nav';
import Home from './components/Home';
import Scenario1 from './components/Scenario1';
import Scenario2 from './components/Scenario2';
import Scenario3 from './components/Scenario3';
import Chart1 from './components/Chart1';
import Chart2 from './components/Chart2';
import Chart3 from './components/Chart3';

import "./App.css"

import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';

function App() {
  return (
    <Router>
      <div className="App">
          <Nav />
          <Switch>
            <Route path="/" exact component={Home} />
            <Route path="/scenario1" exact component={Scenario1} />
            <Route path="/scenario2" exact component={Scenario2} />
            <Route path="/scenario3" exact component={Scenario3} />
            <Route path="/chart1" exact component={Chart1} />
            <Route path="/chart2" exact component={Chart2} />
            <Route path="/chart3" exact component={Chart3} />
          </Switch>

          
      </div>
    </Router>
  );
}

export default App;
