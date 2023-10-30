const express = require('express');
const app = express();
const port = 3000

app.use(express.static('frontend'));

app.get("/",(req,res)=>{
    
})

app.listen(port, (error)=>{
    console.log("Listening on port: "+ port)
    if(error){
        console.log("something went wrong");
    }else{
        console.log("Server is listening on port " + port)
    }
})