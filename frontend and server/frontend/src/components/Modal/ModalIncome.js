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
            <div className="modal-header">
                <p>{city}</p>
                <span onClick={close} class="close-modal-btn">x</span>
            </div>
            <div className="modal-content">
                <div className="modal-body">
                    <h4><u>{city}</u></h4>
                    {
                        show ? 
                        apidata.map((data, key) => {
                            if (data.docs) {
                                return (
                                    <p>
                                    {
                                        data.docs.map((detail, keyDetail) => {
                                            return (
                                                <p>
                                                <div className="label">Year : {detail.year}</div>
                                                <div className="label">Average : {detail.mean_income_yr}</div>
                                                <div><ProgressBar key={keyDetail} bgcolor="#6a1b9a" completed={Number((detail.mean_income_yr/100000)*100).toFixed(2)} /></div>
                                                </p>
                                            );
                                        })
                                        // }
                                    }
                                    </p>
                                );
                            }
                            if (data.sentiment) {
                                return (
                                    <p>
                                    {
                                        data.sentiment.map((detailSentiment, keyDetailSentiment) => {
                                            return (
                                                <p>
                                                <PieChart data={detailSentiment}
                                                />;
                                                </p>
                                            );
                                        })
                                        // }
                                    }
                                    </p>
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