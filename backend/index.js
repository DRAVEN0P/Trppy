// const = require('mongoose');
const app = require('./app');
const UserModel = require("./model/user.model");
const db = require('./config/db');
const port = 3000;


// app.get('/', (req, res) => {
//     res.send("Hello World")
// });

app.listen(port,() => {
    console.log(`listening on port: ${port}`)
})