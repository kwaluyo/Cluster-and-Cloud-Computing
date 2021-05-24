import React, {useState,useEffect} from "react";
import './Modal.css';
import ProgressBar from "../progress-bar.component";
import { PieChart } from 'react-minimal-pie-chart';

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
                                                return(
                                                    <div className="grid-item">
                                                        <div className="pie_block_satisfaction">
                                                            <PieChart data={[
                                                                    {'title': 'Satisfaction 10 PC','value': detail.satisfaction_10_pc,'color': '#E38627'},
                                                                    {'title': 'Satisfaction 20 PC','value': detail.satisfaction_20_pc,'color': '#C13C37'},
                                                                    {'title': 'Satisfaction 30 PC','value': detail.satisfaction_30_pc,'color': '#6A2135'},
                                                                    {'title': 'Satisfaction 40 PC','value': detail.satisfaction_40_pc,'color': '#3A2135'},
                                                                    {'title': 'Satisfaction 50 PC','value': detail.satisfaction_50_pc,'color': '#3A2150'},
                                                                    {'title': 'Satisfaction 60 PC','value': detail.satisfaction_60_pc,'color': '#3A2160'},
                                                                    {'title': 'Satisfaction 70 PC','value': detail.satisfaction_70_pc,'color': '#3A2170'},
                                                                    {'title': 'Satisfaction 80 PC','value': detail.satisfaction_80_pc,'color': '#3A2180'},
                                                                    {'title': 'Satisfaction 90 PC','value': detail.satisfaction_90_pc,'color': '#3A2190'},
                                                                    {'title': 'Satisfaction 100 PC','value': detail.satisfaction_100_pc,'color': '#3A2235'}
                                                                ]   }
                                                                    label={(data) => data.dataEntry.value}
                                                                    labelPosition={65}
                                                                    labelStyle={{
                                                                    fontSize: "6px",
                                                                    fontColor: "FFFFFA",
                                                                    fontWeight: "500",
                                                                    }}
                                                            />
                                                        </div>
                                                        <div className="pie_block_satisfaction">
                                                            <PieChart data={[
                                                                    {'title': 'Compound','value': detail.years.sentiment.compound,'color': '#E38627'},
                                                                    {'title': 'Negative','value': detail.years.sentiment.negative,'color': '#C13C37'},
                                                                    {'title': 'Neutral','value': detail.years.sentiment.neutral,'color': '#6A2135'},
                                                                    {'title': 'Positive','value': detail.years.sentiment.positive,'color': '#3A2135'}]}
                                                                    label={(data) => data.dataEntry.value.toFixed(2)}
                                                                    labelPosition={65}
                                                                    labelStyle={{
                                                                    fontSize: "6px",
                                                                    fontColor: "FFFFFA",
                                                                    fontWeight: "500",
                                                                    }}
                                                            />
                                                        </div>
                                                    </div>
                                                );
                                            } else {
                                                return(
                                                    <div className="grid-item">
                                                        <div className="pie_block_satisfaction">
                                                        <PieChart data={[
                                                                    {'title': 'Satisfaction 10 PC','value': detail.satisfaction_10_pc,'color': '#E38627'},
                                                                    {'title': 'Satisfaction 20 PC','value': detail.satisfaction_20_pc,'color': '#C13C37'},
                                                                    {'title': 'Satisfaction 30 PC','value': detail.satisfaction_30_pc,'color': '#6A2135'},
                                                                    {'title': 'Satisfaction 40 PC','value': detail.satisfaction_40_pc,'color': '#3A2135'},
                                                                    {'title': 'Satisfaction 50 PC','value': detail.satisfaction_50_pc,'color': '#3A2150'},
                                                                    {'title': 'Satisfaction 60 PC','value': detail.satisfaction_60_pc,'color': '#3A2160'},
                                                                    {'title': 'Satisfaction 70 PC','value': detail.satisfaction_70_pc,'color': '#3A2170'},
                                                                    {'title': 'Satisfaction 80 PC','value': detail.satisfaction_80_pc,'color': '#3A2180'},
                                                                    {'title': 'Satisfaction 90 PC','value': detail.satisfaction_90_pc,'color': '#3A2190'},
                                                                    {'title': 'Satisfaction 100 PC','value': detail.satisfaction_100_pc,'color': '#3A2235'}
                                                                ]   }
                                                                    label={(data) => data.dataEntry.value}
                                                                    labelPosition={65}
                                                                    labelStyle={{
                                                                    fontSize: "6px",
                                                                    fontColor: "FFFFFA",
                                                                    fontWeight: "500",
                                                                    }}
                                                            />
                                                            </div>
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