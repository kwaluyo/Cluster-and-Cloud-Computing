import React, {useState,useEffect} from "react";
import './Modal.css';
import ProgressBar from "../progress-bar.component";
import { PieChart } from 'react-minimal-pie-chart';

// export default Modal;
export const Modal = ({ show, city, apidata,close }) => {
    return  (
        <div className="modal-wrapper-support"
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
                                    <div className="grid-container-support">
                                    {
                                        data.docs.map((detail, keyDetail) => {
                                            if(detail.years) {
                                                return(
                                                    <div className="grid-item">
                                                        <div className="">Year : {detail.year}</div>
                                                        <div className="grid-item-1">
                                                            <div className="data_block">
                                                                <div className="label">Pension</div>
                                                                <div className="progbar"><ProgressBar key={key} bgcolor="#6a1b9a" completed={Number(detail.age_pension_pc).toFixed(2)} /></div>
                                                            </div>
                                                            <div className="data_block">
                                                                <div className="label">Senior Card</div>
                                                                <div className="progbar"><ProgressBar key={key} bgcolor="#6a1b9a" completed={Number(detail.senior_card).toFixed(2)} /></div>
                                                            </div>
                                                            <div className="data_block">
                                                                <div className="label">Disable</div>
                                                                <div className="progbar"><ProgressBar key={key} bgcolor="#6a1b9a" completed={Number(detail.disable).toFixed(2)} /></div>
                                                            </div>
                                                            <div className="data_block">
                                                                <div className="label">Sole Fam</div>
                                                                <div className="progbar"><ProgressBar key={key} bgcolor="#6a1b9a" completed={Number(detail.sole_fam).toFixed(2)} /></div>
                                                            </div>
                                                            <div className="data_block">
                                                                <div className="label">Unemployment</div>
                                                                <div className="progbar"><ProgressBar key={key} bgcolor="#6a1b9a" completed={Number(detail.unemployment).toFixed(2)} /></div>
                                                            </div>
                                                        </div>
                                                        <div className="grid-item-2">
                                                            <PieChart data={[
                                                                    // {'title': 'Compound','value': detail.years.sentiment.compound,'color': '#E38627'},
                                                                    {'title': 'Negative','value': detail.years.sentiment.negative,'color': '#F74749'},
                                                                    {'title': 'Neutral','value': detail.years.sentiment.neutral,'color': '#FDB45C'},
                                                                    {'title': 'Positive','value': detail.years.sentiment.positive,'color': '#47BEBE'}]}
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
                                            } else {
                                                return(
                                                    <div className="grid-item">
                                                        <div className="">Year : {detail.year}</div>
                                                        <div className="grid-item-1">
                                                            <div className="data_block">
                                                                <div className="label">Pension</div>
                                                                <div className="progbar"><ProgressBar key={key} bgcolor="#6a1b9a" completed={Number(detail.age_pension_pc).toFixed(2)} /></div>
                                                            </div>
                                                            <div className="data_block">
                                                                <div className="label">Senior Card</div>
                                                                <div className="progbar"><ProgressBar key={key} bgcolor="#6a1b9a" completed={Number(detail.senior_card).toFixed(2)} /></div>
                                                            </div>
                                                            <div className="data_block">
                                                                <div className="label">Disable</div>
                                                                <div className="progbar"><ProgressBar key={key} bgcolor="#6a1b9a" completed={Number(detail.disable).toFixed(2)} /></div>
                                                            </div>
                                                            <div className="data_block">
                                                                <div className="label">Sole Fam</div>
                                                                <div className="progbar"><ProgressBar key={key} bgcolor="#6a1b9a" completed={Number(detail.sole_fam).toFixed(2)} /></div>
                                                            </div>
                                                            <div className="data_block">
                                                                <div className="label">Unemployment</div>
                                                                <div className="progbar"><ProgressBar key={key} bgcolor="#6a1b9a" completed={Number(detail.unemployment).toFixed(2)} /></div>
                                                            </div>
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