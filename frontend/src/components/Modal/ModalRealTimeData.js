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
                            if (data.docs) {
                                return (
                                    <div className="grid-container-realdata">
                                    {
                                        data.docs.map((detail, keyDetail) => {
                                            return(
                                                <div className="grid-item">
                                                    <div className="pie_block_satisfaction">
                                                        <p>Compound : {detail.compound.toFixed(2)}</p>
                                                        <PieChart data={[
                                                                    // {'title': 'Compound','value': detail.compound,'color': '#E38627'},
                                                                    {'title': 'Negative','value': detail.negative,'color': '#C13C37'},
                                                                    {'title': 'Neutral','value': detail.neutral,'color': '#6A2135'},
                                                                    {'title': 'Positive','value': detail.positive,'color': '#3A2135'}]}
                                                                    label={(data) => data.dataEntry.value.toFixed(2)}
                                                                    labelPosition={65}
                                                                    labelStyle={{
                                                                    fontSize: "10px",
                                                                    fontColor: "FFFFFA",
                                                                    fontWeight: "500",
                                                                    }}
                                                            />
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