import React from 'react';
import {useEffect, useState} from 'react';
import "../App.css"

function Home(){

    return(
        <div className="content">
            <div className="content1"> Find the happiest city</div>
            <div className="subcontent">
                <div className="content2"> 
                <h4>Group 17</h4>
                    <h6>Jeanelle Abanto: 1133815</h6>
                    <h6>Kartika Waluyo: 1000555</h6>
                    <h6>Radhimas Djan: 1146240</h6>
                    <h6>Zi Jin: 987771</h6>                    
                </div>
                <div className="content3"> The project is to explore the happiness of 4 cities in australia, based on their sentiment we will compare them with the aurin data that can be correlated we will use a 2014~2018 data for comparing with the aurin while we will be using a harvester to get a 2021 data and analyze their sentiment</div>                {/* <div className="content4"> content4 </div>
                {/* <div className="content4"> content4 </div>
                <div className="content5"> content5 </div> */}
            </div>
        </div>

    );
}

export default Home;