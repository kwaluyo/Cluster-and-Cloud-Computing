import React, {useState,useEffect} from 'react';
// let textApi = '';

function Scenario4() {
    const [textApi,setTextApi] = useState(null)
    useEffect(() => {
        fetch('/api/data/all').then(response =>
            response.json().then(data=>{
                setTextApi(data[0].text);
                console.log(data[0].text);

            }))
    },[]);


    return (
        <div className="App">{textApi}</div>
    );
}

export default Scenario4;