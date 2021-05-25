import React, {useState,useEffect} from "react";
import './Modal.css';
import ProgressBar from "../progress-bar.component";
// import { PieChart } from 'react-minimal-pie-chart';
import { Pie, defaults } from 'react-chartjs-2';
import { chartColors } from "../colors";
// export default Modal;


export const Modal = ({ show, city, apidata,close }) => {
    return  (
        <div className="modal-wrapper"
            style={{
                display: show ? 'block':'none'
            }}>
            {/* <div className="modal-header">
                <p>{city}</p>
                <span onClick={close} class="close-modal-btn">x</span>
            </div> */}
            <div className="modal-content">
                <div className="modal-body">
                    <h4><u>{city}</u></h4>
                    {
                        show ? 
                        apidata.map((data, key) => {
                            console.log(data);
                            if (data.docs) {
                                return (
                                    <div className="grid-container">
                                    {
                                        data.docs.map((detail, keyDetail) => {
                                            if(detail.years) {
                                                // defaults.global.legend.position = "bottom"
                                                let chartInstance = null;
                                                const pieOptions = {
                                                    legend: {
                                                      display: true,
                                                      position: "left"
                                                    },
                                                    elements: {
                                                      arc: {
                                                        borderWidth: 0
                                                      }
                                                    }
                                                  };
                                                  
                                                  const data = {
                                                    maintainAspectRatio: false,
                                                    responsive: false,
                                                    labels: ["Negative", "Neutral", "Positive"],
                                                    datasets: [
                                                      {
                                                        data: [
                                                            (detail.years.sentiment.negative/detail.total),
                                                            (detail.years.sentiment.neutral/detail.total),
                                                            (detail.years.sentiment.positive/detail.total)],
                                                        backgroundColor: chartColors,
                                                        hoverBackgroundColor: chartColors
                                                      }
                                                    ]
                                                  };
                                                return(
                                                    <div className="grid-item">
                                                        <div className="label">Year : {detail.year}</div>
                                                        <div className="label">Income Average : {detail.mean}</div>
                                                        {/* <div><ProgressBar key={keyDetail} bgcolor="#6a1b9a" completed={Number((detail.mean/100000)*100).toFixed(2)} /></div> */}
                                                        <div className="pie_block">
                                                            <Pie
                                                                data={data}
                                                                options={pieOptions}
                                                                ref={input => {
                                                                chartInstance = input;
                                                                }}
                                                            />
                                                        {/* <PieChart data={[
                                                                    {'title': 'Compound','value': detail.years.sentiment.compound,'color': '#E38627'},
                                                                    {'title': 'Negative','value': detail.years.sentiment.negative,'color': '#C13C37'},
                                                                    {'title': 'Neutral','value': detail.years.sentiment.neutral,'color': '#6A2135'},
                                                                    {'title': 'Positive','value': detail.years.sentiment.positive,'color': '#3A2135'}]}
                                                                    label={(data) => data.dataEntry.value.toFixed(2)}
                                                                    labelPosition={65}
                                                                    labelStyle={{
                                                                    fontSize: "8px",
                                                                    fontColor: "FFFFFA",
                                                                    fontWeight: "auto",
                                                                    }}
                                                            /> */}
                                                        </div>
                                                    </div>
                                                );
                                            } else {
                                                return(
                                                    <div className="grid-item">
                                                        <div className="label">Year : {detail.year}</div>
                                                        <div className="label">Income Average : {detail.mean}</div>
                                                        {/* <div><ProgressBar key={keyDetail} bgcolor="#6a1b9a" completed={Number((detail.mean/100000)*100).toFixed(2)} /></div> */}
                                                    </div>
                                                );
                                            }
                                        })
                                    }
                                    </div>
                                );
                            }
                        }): ''  
                    }
                </div>
                <div className="modal-footer">
                    <button onClick={close} className="btn-cancel">Close</button>
                </div>
            </div>
        </div>
    )
};