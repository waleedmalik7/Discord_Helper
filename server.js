const express = require('express');
const path = require('path');
const app = express();
const port = 3000

app.use(express.urlencoded({ extended: true}))
app.use(express.static('frontend'));

app.get("/",(req,res)=>{
    res.sendFile(path.join(__dirname, "/frontend/connect.html"));
})

app.post("/delete",(req,res)=>{
    console.log(req.body.channel, req.body.token);
})

app.listen(port, (error)=>{
    console.log("Listening on port: "+ port)
    if(error){
        console.log("something went wrong");
    }else{
        console.log("Server is listening on port " + port)
    }
})