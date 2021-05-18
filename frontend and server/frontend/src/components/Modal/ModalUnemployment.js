import React, {useState,useEffect} from "react";
import './Modal.css';
import ProgressBar from "../progress-bar.component";

// const Modal = ({ handleClose, show, children }) => {
//   const showHideClassName = show ? "modal d-block" : "modal d-none";

//   return (
//     <div className={showHideClassName}>
//       <div className="modal-container">
//         {children}
//         <a href="javascript:;" className="modal-close" onClick={handleClose}>
//           close
//         </a>
//       </div>
//     </div>
//   );
// };

function getAPI() {
    
}

// export default Modal;
export const Modal = ({ show, city, apidata,close }) => {
    if (show == true) {
          // React.useEffect(() => {
            // fetch('/api/data?city='+city).then(response =>
            //     response.json().then(data=>{
            //         console.log(data)
            // }))
        // },[]);
    }
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
                                <div className="label">Year : {data.year}</div>
                                {/* <div className="label">Average Num: {data.avg_unemp_num}</div> */}
                                <div className="label">Average Rate: {data.avg_unemp_rate}</div>
                                <div><ProgressBar key={key} bgcolor="#6a1b9a" completed={Number(data.avg_unemp_rate).toFixed(2)} /></div>
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