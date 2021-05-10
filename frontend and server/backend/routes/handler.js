const express = require('express');
const router = express.Router();


router.get('/scenario1', (req, res) => {
    const str = [
        {
            "name": "Map 1",
            "msg": "This is the map for scenario 1",
            "username": ""
        }
    ];
    res.end(JSON.stringify(str));
    // const str = "Map 1"
    // res.end(str)
    
});

router.get('/scenario2', (req, res) => {
    const str = [
        {
            "name": "Map 2",
            "msg": "This is the map for scenario 2",
            "username": ""
        }
    ];
    res.end(JSON.stringify(str));
    // const str = "Map 1"
    // res.end(str)
    
});

router.get('/scenario3', (req, res) => {
    const str = [
        {
            "name": "Map 3",
            "msg": "This is the map for scenario 3",
            "username": ""
        }
    ];
    res.end(JSON.stringify(str));
    // const str = "Map 1"
    // res.end(str)
    
});

router.get('/chart3', (req, res) => {
    const str = [
        {
            "name": "Chart 3",
            "msg": "This is the chart for scenario 3",
            "username": ""
        }
    ];
    res.end(JSON.stringify(str));
});

router.get('/chart2', (req, res) => {
    const str = [
        {
            "name": "Chart 2",
            "msg": "This is the chart for scenario 2",
            "username": ""
        }
    ];
    res.end(JSON.stringify(str));
});

router.get('/chart1', (req, res) => {
    const str = [
        {
            "name": "Chart 1",
            "msg": "This is the chart for scenario 1",
            "username": ""
        }
    ];
    res.end(JSON.stringify(str));
});

module.exports = router;