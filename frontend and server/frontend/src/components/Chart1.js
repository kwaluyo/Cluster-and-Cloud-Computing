import React, { PureComponent, useEffect, useState} from 'react';
// import {Link} from 'react-router-dom';
import { BarChart, Bar, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import * as Income from '../data/sentiment-income.json'
import "../App.css"

const data = Income.cities


function Chart1() {
    useEffect( () => {
        fetchItems();
    }, []);

    const [items, setItems] = useState([]);

    const fetchItems = async () => {
        const data = await fetch('/chart1');
        const items = await data.json();
        setItems(items);
    };


    return (
        <div>
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

            <div className="barchart"> 
            <BarChart
                width={1000}
                height={500}
                data={data}
                margin={{
                    top: 5,
                    right: 30,
                    left: 20,
                    bottom: 5
                }}
                >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis xAxisId="0" dataKey="year" />
                <XAxis xAxisId="1" dataKey="name" allowDuplicatedCategory={false} />
                <YAxis />
                <Tooltip />
                <Legend />
                <Bar dataKey="income" fill="#594422" />
                <Bar dataKey="sentiment" fill="#B18743" />
            </BarChart>
            </div>   
        </div>
        
      );
}



export default Chart1;