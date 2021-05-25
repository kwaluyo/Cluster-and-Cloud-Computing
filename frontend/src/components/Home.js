import React from 'react';
import {useEffect, useState} from 'react';
import "../App.css"


function Home(){

    return(
        <div className="content">
            <div className="subcontent1">
                <div className="subcontent1-1">
                    <img className="twitter-img" src="/twitter.jpg" alt="Twitter Icon" />
                </div>
                <div className="subcontent1-2">
                    <div className="content1"> Happiest</div>
                    <div className="content1-1"> City</div>
                </div>
            </div>
     

            <div className="subcontent2">
                <div className="content2"> 
                <h4>Group 17</h4>
                    <h6>Jeanelle Abanto: 1133815</h6>
                    <h6>Kartika Waluyo: 1000555</h6>
                    <h6>Radhimas Djan: 1146240</h6>
                    <h6>Zi Jin: 987771</h6>                    
                </div>
                <div className="content3"> Exploring the happiness of 4 big cities' residents in Australia, based on the sentiment analysis from tweets. The tweets from each city are then correlated with some aurin data from 2014 to 2018. Making use of a harvester, 2021 data are collected and their sentiments are analysed.</div>                {/* <div className="content4"> content4 </div>
                {/* <div className="content4"> content4 </div>
                <div className="content5"> content5 </div> */}
            </div>
        </div>

    );
}

export default Home;