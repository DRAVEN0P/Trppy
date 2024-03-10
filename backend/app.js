const express = require('express');
const bodyParser = require('body-parser'); // Changed import name
const userRoute = require('./routes/user.routes');

const app = express();

// app.use(bodyParser.json()); // Use bodyParser middleware for JSON parsing
app.use(bodyParser.json());
app.use('/', userRoute); // Mount user routes at the root URL

module.exports = app; // Export the Express app
