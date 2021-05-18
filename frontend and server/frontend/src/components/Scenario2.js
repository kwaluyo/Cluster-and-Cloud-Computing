import React, { useState, useEffect } from "react";
import ReactMapGL, { Marker, Popup } from "react-map-gl";
import * as Cities from '../data/cities.json'
import mapboxgl from 'mapbox-gl/dist/mapbox-gl-csp';
import { Link } from 'react-router-dom';
import { Modal } from './Modal/ModalSatisfaction';

function Scenario2() {
  const [viewport, setViewport] = useState({
    latitude: -25.9958,
    longitude: 135.1745,
    width: '100vw',
    height: '100vh',
    zoom: 3.5
  });
  const [selectedCity, setSelectedCity] = useState(null);
  const [show,setShow] = useState(false)
  const [city,setCity] = useState(null)
  const [apiData,setApiData] = useState(null)

  useEffect(() => {
    getGitHubUserWithFetch();
  }, []);

  const getGitHubUserWithFetch = async (cityName) => {
    const response = await fetch('/api/satisfaction?city='+cityName);
    const jsonData = await response.json();
    console.log(jsonData);
    setApiData(jsonData);
  };
  
  useEffect(() => {
    const listener = e => {
      if (e.key === "Escape") {
        setSelectedCity(null);
      }
    };
    window.addEventListener("keydown", listener);

    return () => {
      window.removeEventListener("keydown", listener);
    };
  }, []);

  useEffect( () => {
    fetchItems();
    }, []);

  const [items, setItems] = useState([]);

  const fetchItems = async () => {
      const data = await fetch('/scenario1');
      // if (!data.ok) {
      //   const message = `An error has occured: ${data.status}`;
      //   throw new Error(message);
      // }
      const items = await data.json();
      setItems(items);
  };

  const closeModalHadler = () => setShow(false);
  
  return (
    
    <div>
      <Modal show={show} city={city} apidata={apiData} close={closeModalHadler}/>
      <div>
          {
            items.map(item => (
                <div class="container-fluid p-3 w-50">
                    <div class="card-deck">
                        <div class="card">
                            <div class="card-body p-1">
                                <h6 class="card-title">{item.name}</h6>
                                <p class="card-text">{item.msg}</p>
                                <p class="card-text"><i>{item.username}</i></p>
                            </div>
                        </div>
                    </div>
                </div>
            ))
            }
      </div>
      <ReactMapGL
        {...viewport}
        mapboxApiAccessToken='pk.eyJ1Ijoia3dhbHV5byIsImEiOiJja28zejVrZjMwMmVoMnFxd3kwaDlzM2RmIn0.CpCst2zLMvWrjhmTwaWCCg'
        mapStyle="mapbox://styles/kwaluyo/cko474hnl0w3v18qqg8o0mwhe"
        onViewportChange={viewport => {
          setViewport(viewport);
        }}
      >
        {Cities.cities.map(city => (
          <Marker onClick={() => setShow(true)}
            key = {city.ID}
            latitude = {city.coordinate.lat}
            longitude = {city.coordinate.lng}
          >
            <button
              className="marker-btn"
              onClick={e => {
                setSelectedCity(city);
                setCity(city.name);
                getGitHubUserWithFetch(city.name);
                e.preventDefault();
              }}
            
            >
              <img src="/mapbox-marker-icon-20px-gray.png" alt="City Icon" />
            </button>
          </Marker>
        ))}

        {/* erased selectedCity */}
      </ReactMapGL>
    </div>
  );
}

export default Scenario2;