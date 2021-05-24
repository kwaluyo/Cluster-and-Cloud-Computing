import React, {useState,useEffect} from "react";
import './Modal.css';
import ProgressBar from "../progress-bar.component";

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
                            return (
                            <p>
                                <div className="data_block">
                                    <div className="label">Satisfaction 10 PC ({data.satisfaction_10_pc})</div>
                                    <div className="progbar"><ProgressBar key={key} bgcolor="#6a1b9a" completed={Number(data.satisfaction_10_pc).toFixed(2)} /></div>
                                </div>
                                <div className="data_block">
                                    <div className="label">Satisfaction 20 PC ({data.satisfaction_20_pc})</div>
                                    <div className="progbar"><ProgressBar key={key} bgcolor="#6a1b9a" completed={Number(data.satisfaction_20_pc).toFixed(2)} /></div>
                                </div>
                            </p>
                            );
                        }) : ''
                        }
                </div>
                <div className="modal-footer">
                    <button onClick={close} className="btn-cancel">Close</button>
                </div>
            </div>
        </div>
    )
};