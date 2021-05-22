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
                            console.log(data);
                            if (data.docs) {
                                return (
                                    <div className="content_block">
                                    {
                                        data.docs.map((detail, keyDetail) => {
                                            
                                            return (
                                                <p>
                                                    
                                                <div className="label">Year : {detail.year}</div>
                                                <div className="label">Average : {detail.mean}</div>
                                                <div><ProgressBar key={keyDetail} bgcolor="#6a1b9a" completed={Number((detail.mean/100000)*100).toFixed(2)} /></div>
                                                </p>
                                                
                                            );
                                        })
                                        // }
                                    }
                                    {
                                        data.docs.map((detail, keyDetail) => {
                                            if (detail.years.sentiment)
                                                return (
                                                    <p>
                                                        <PieChart data={[
                                                            {'title': 'Compound','value': detail.years.sentiment.compound,'color': '#E38627'},
                                                            {'title': 'Negative','value': detail.years.sentiment.negative,'color': '#C13C37'},
                                                            {'title': 'Neutral','value': detail.years.sentiment.neutral,'color': '#6A2135'},
                                                            {'title': 'Positive','value': detail.years.sentiment.positive,'color': '#3A2135'}]}/>
                                                    </p>
                                                
                                            );
                                        })
                                    }
                                    </div>
                                );
                            }
                            // if (data.sentiment) {
                            //     return (
                            //         <div className="pie_content_block">
                            //         {
                            //             data.sentiment.map((detailSentiment, keyDetailSentiment) => {
                            //                 return (
                            //                     <p>
                            //                     <PieChart data={detailSentiment} label={(data) => data.dataEntry.value.toFixed(2)}
                            //                     labelPosition={65}
                            //                     labelStyle={{
                            //                       fontSize: "5px",
                            //                       fontColor: "FFFFFA",
                            //                       fontWeight: "500",
                            //                     }}
                            //                     />;
                            //                     </p>
                            //                 );
                            //             })
                            //             // }
                            //         }
                            //         </div>
                            //     );
                            // }
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