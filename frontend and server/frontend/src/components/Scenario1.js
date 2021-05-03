import React, {useEffect, useState} from 'react';
import {GoogleMap, withScriptjs, withGoogleMap} from 'react-google-maps';
// import {Link} from 'react-router-dom';


function Map() {
    return <GoogleMap 
    bootstrapURLKeys={{ key: 'AIzaSyCf_6Wwh25_JH-W2gIOUGtbeqZ-Pu3nhHU' }}
    defaultZoom={10} 
    defaultCenter={{lat:-37.81411, lng:144.96328}}
    >
    </GoogleMap>
}

const WrappedMap = withScriptjs(withGoogleMap(Map))


function Scenario1() {
    useEffect( () => {
        fetchItems();
    }, []);

    const [items, setItems] = useState([]);

    const fetchItems = async () => {
        const data = await fetch('/scenario1');
        const items = await data.json();
        setItems(items);
    };

    return(
        <section>
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
            <div style={{width:'100vw', height:'100vh'}}>
                <WrappedMap googleMapURL={'https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places'}
                loadingElement ={ <div style={{ height: `100%` }} />}
                containerElement ={ <div style={{ height: `400px` }} />}
                mapElement ={ <div style={{ height: `100%` }} />}

                />
            </div>
        </section>
    );
}



export default Scenario1;
