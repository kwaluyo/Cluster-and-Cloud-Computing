import React from 'react';
import {useEffect, useState} from 'react';
import "../App.css"

function Home(){

    return(
        <div className="content">
            <div className="content1"> Project Title </div>
            <div className="subcontent">
                <div className="content2"> 
                    <h4>Group x</h4>
                    <h6>Member 1: Student id 1</h6>
                    <h6>Member 2: Student id 2</h6>
                    <h6>Member 3: Student id 3</h6>
                    <h6>Member 4: Student id 4</h6>
                    
                </div>
                <div className="content3"> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Integer vitae justo eget magna fermentum iaculis eu non diam. At lectus urna duis convallis convallis tellus id interdum. Fermentum iaculis eu non diam. Ullamcorper eget nulla facilisi etiam. Urna et pharetra pharetra massa massa ultricies. Tristique et egestas quis ipsum. Sed odio morbi quis commodo odio. Venenatis cras sed felis eget velit aliquet sagittis. Massa eget egestas purus viverra accumsan in nisl nisi scelerisque. Volutpat blandit aliquam etiam erat velit scelerisque in dictum. Gravida cum sociis natoque penatibus. Etiam dignissim diam quis enim. </div>
                {/* <div className="content4"> content4 </div>
                <div className="content5"> content5 </div> */}
            </div>
        </div>

    );
}

export default Home;