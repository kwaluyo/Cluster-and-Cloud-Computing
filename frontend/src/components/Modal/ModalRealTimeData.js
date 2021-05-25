import React, {useState,useEffect} from "react";
import './Modal.css';
import { Pie } from 'react-chartjs-2';
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
                            if (data.docs) {
                                return (
                                    <div className="grid-container-realdata">
                                    {
                                        data.docs.map((detail, keyDetail) => {
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
                                                            detail.negative,
                                                            detail.neutral,
                                                            detail.positive
                                                        ],
                                                        backgroundColor: chartColors,
                                                        hoverBackgroundColor: chartColors
                                                      }
                                                    ]
                                                  };
                                            return(
                                                <div className="grid-item">
                                                    <div className="pie_block_satisfaction">
                                                        <p>Compound : {detail.compound.toFixed(2)}</p>
                                                        <Pie
                                                                data={data}
                                                                options={pieOptions}
                                                                ref={input => {
                                                                chartInstance = input;
                                                                }}
                                                            />
                                                        {/* <PieChart data={[
                                                                    // {'title': 'Compound','value': detail.compound,'color': '#E38627'},
                                                                    {'title': 'Negative','value': detail.negative,'color': '#F74749'},
                                                                    {'title': 'Neutral','value': detail.neutral,'color': '#FDB45C'},
                                                                    {'title': 'Positive','value': detail.positive,'color': '#47BEBE'}]}
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