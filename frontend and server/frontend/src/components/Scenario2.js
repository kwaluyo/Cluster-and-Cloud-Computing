import React, { useRef, useEffect, useState } from 'react';
import ReactDOM from 'react-dom';
import mapboxgl from 'mapbox-gl/dist/mapbox-gl-csp';
// eslint-disable-next-line import/no-webpack-loader-syntax
import MapboxWorker from 'worker-loader!mapbox-gl/dist/mapbox-gl-csp-worker';
import * as Cities from '../data/cities.json'
import ReactMapGl, {Marker} from 'react-map-gl'
mapboxgl.workerClass = MapboxWorker;
mapboxgl.accessToken = 'pk.eyJ1Ijoia3dhbHV5byIsImEiOiJja28zejVrZjMwMmVoMnFxd3kwaDlzM2RmIn0.CpCst2zLMvWrjhmTwaWCCg';

const Map = () => {
  const mapContainer = useRef();
  const [lng, setLng] = useState(135.1745);
  const [lat, setLat] = useState(-25.9958);
  const [zoom, setZoom] = useState(4);

  useEffect(() => {
    const map = new mapboxgl.Map({
      container: mapContainer.current,
      style: 'mapbox://styles/mapbox/streets-v11',
      center: [lng, lat],
      zoom: zoom
    });

    map.on('move', () => {
      setLng(map.getCenter().lng.toFixed(4));
      setLat(map.getCenter().lat.toFixed(4));
      setZoom(map.getZoom().toFixed(2));
    });

    return () => map.remove();
    // eslint-disable-next-line
  }, []);

  return (
    <div>
      <div className="sidebar">
        Longitude: {lng} | Latitude: {lat} | Zoom: {zoom}
      </div>
      <div className="map-container" ref={mapContainer} >
          {/* {Cities.cities.map(city => (
              <Marker
                  key = {city.ID}
                  latitude = {city.lat}
                  longitude = {city.lng}
                >
                    <div>
                     AAAAAAAAAAA   
                    </div>
              </Marker>
          ))} */}
      </div>
    </div>
  );
};

ReactDOM.render(<Map />, document.getElementById('root'));


// function Scenario2() {
//     useEffect( () => {
//         fetchItems();
//     }, []);

//     const [items, setItems] = useState([]);

//     const fetchItems = async () => {
//         const data = await fetch('/scenario2');
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

export default Map;