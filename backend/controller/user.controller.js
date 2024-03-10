const UserService = require("../services/user.services")


// exports.register = async(req,res,next)=>{
//     try{
//         const { email, password } = req.body;
//         const successRes = await UserService.registerUser(email,password);
//         res.json({status:true,success:"User Registered successfully"})
//     }catch(err){
//         throw err;
//     }
// }
// const UserService = require('./path/to/user.service');

module.exports.register = async (req, res, next) => {
    try {
        const {email,password} = req.body;
        console.log(req);

        // Check if email and password are provided
        if (!email || !password) {
            return res.status(400).json({ status: false, error: "Email and password are required" });
        }

        // Call the service to register the user
        const successRes = await UserService.registerUser(email, password);

        // Send a success response
        res.json({ status: true, success: "User registered successfully" });
    } catch (err) {
        // Handle any errors
        console.error("Error during user registration:", err);
        res.status(500).json({ status: false, error: "Internal server error" });
    }
};

