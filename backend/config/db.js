const mongoose = require('mongoose');

const connection = mongoose.createConnection("mongodb://localhost:27017/newTd").on('open',() => {
    console.log("Connected to MongoDB");
});
module.exports = connection;