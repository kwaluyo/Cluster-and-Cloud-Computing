import React from 'react'; // ES6 js
import {Link} from 'react-router-dom';

function Nav() {
    return(
        <nav class="navbar navbar-expand-lg navbar-dark">
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navMainMenu" aria-controls="navMainMenu" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div id="navMainMenu" class="navbar-collapse collapse">
                <div class="navbar-nav">
                    <Link to='/' className="nav-item nav-link">Home</Link>
                    <Link to='/scenario1' className="nav-item nav-link">Scenario 1</Link>
                    <Link to='/scenario2' className="nav-item nav-link">Scenario 2</Link>
                    <Link to='/scenario3' className="nav-item nav-link">Scenario 3</Link>
                    <Link to='/scenario4' className="nav-item nav-link">Scenario 4</Link>
                </div>
            </div>
        </nav>
    );
}

export default Nav;
