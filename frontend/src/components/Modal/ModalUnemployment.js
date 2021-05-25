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
                                                        <div className="label">Year : {detail.year}</div>
                                                        <div className="label">Average : {detail.rate}</div>
                                                        <div><ProgressBar key={keyDetail} bgcolor="#6a1b9a" completed={detail.rate.toFixed(2)} /></div>
                                                        <div className="pie_block">
                                                        <PieChart data={[
                                                                    // {'title': 'Compound','value': detail.years.sentiment.compound,'color': '#E38627'},
                                                                    {'title': 'Negative','value': detail.years.sentiment.negative,'color': '#F74749'},
                                                                    {'title': 'Neutral','value': detail.years.sentiment.neutral,'color': '#FDB45C'},
                                                                    {'title': 'Positive','value': detail.years.sentiment.positive,'color': '#47BEBE'}]}
                                                                    label={(data) => data.dataEntry.value.toFixed(2)}
                                                                    labelPosition={65}
                                                                    labelStyle={{
                                                                    fontSize: "8px",
                                                                    fontColor: "FFFFFA",
                                                                    fontWeight: "auto",
                                                                    }}
                                                            />
                                                        </div>
                                                    </div>
                                                );
                                            } else {
                                                return(
                                                    <div className="grid-item">
                                                        <div className="label">Year : {detail.year}</div>
                                                        <div className="label">Average : {detail.rate}</div>
                                                        <div><ProgressBar key={keyDetail} bgcolor="#6a1b9a" completed={Number((detail.rate/100000)*100).toFixed(2)} /></div>
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