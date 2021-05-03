import React, { useState, useEffect } from "react";
import ReactMapGL, { Marker, Popup } from "react-map-gl";
import * as Cities from '../data/cities.json'
import mapboxgl from 'mapbox-gl/dist/mapbox-gl-csp';



function Scenario3() {
  const [viewport, setViewport] = useState({
    latitude: -25.9958,
    longitude: 135.1745,
    width: '100vw',
    height: '100vh',
    zoom: 3.5
  });
  const [selectedCity, setSelectedCity] = useState(null);

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
        const data = await fetch('/scenario3');
        const items = await data.json();
        setItems(items);
    };

  return (
    <div>
      {/* <div>
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
      </div> */}
      <ReactMapGL
        {...viewport}
        mapboxApiAccessToken='pk.eyJ1Ijoia3dhbHV5byIsImEiOiJja28zejVrZjMwMmVoMnFxd3kwaDlzM2RmIn0.CpCst2zLMvWrjhmTwaWCCg'
        mapStyle="mapbox://styles/kwaluyo/cko474hnl0w3v18qqg8o0mwhe"
        onViewportChange={viewport => {
          setViewport(viewport);
        }}
      >
        {Cities.cities.map(city => (
          <Marker
            key = {city.ID}
            latitude = {city.coordinate.lat}
            longitude = {city.coordinate.lng}
          >
            <button
              className="marker-btn"
              onClick={e => {
                e.preventDefault();
                setSelectedCity(city);
              }}
            >
              <img src="/mapbox-marker-icon-20px-gray.png" alt="City Icon" />
            </button>
          </Marker>
        ))}

        {selectedCity ? (
          <Popup
            latitude={selectedCity.coordinate.lat}
            longitude={selectedCity.coordinate.lng}
            onClose={() => {
              setSelectedCity(null);
            }}
          >
            <div>
              <h2>{selectedCity.name}</h2>
              <p>This is {selectedCity.name} </p>
            </div>
          </Popup>
        ) : null}
      </ReactMapGL>
    </div>
  );
}


// function Scenario3() {
//     useEffect( () => {
//         fetchItems();
//     }, []);

//     const [items, setItems] = useState([]);

//     const fetchItems = async () => {
//         const data = await fetch('/scenario3');
//         const items = await data.json();
//         setItems(items);
//     };

//     return(
//         <section>
//             {
//             items.map(item => (
//                 <div class="container-fluid p-3 w-50">
//                     <div class="card-deck">
//                         <div class="card">
//                             <div class="card-body p-1">
//                                 <h6 class="card-title">{item.name}</h6>
//                                 <p class="card-text">{item.msg}</p>
//                                 <p class="card-text"><i>{item.username}</i></p>
//                             </div>
//                         </div>
//                     </div>
//                 </div>
//             ))
//             }
//         </section>
//     );
// }

export default Scenario3;