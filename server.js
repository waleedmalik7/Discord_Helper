const express = require('express');
const app = express();
const port = 3000

app.get("/",(req,res)=>{
    res.status(200).send('<h1>Hi</h1>')
})

app.listen(port, (error)=>{
    console.log("Listening on port: "+ port)
    if(error){
        console.log("something went wrong");
    }else{
        console.log("Server is listening on port " + port)
    }
})