import React, {useEffect, useState} from 'react';
// import {Link} from 'react-router-dom';




function Chart3() {
    useEffect( () => {
        fetchItems();
    }, []);

    const [items, setItems] = useState([]);

    const fetchItems = async () => {
        const data = await fetch('/chart3');
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
            
        </section>
    );
}



export default Chart3;