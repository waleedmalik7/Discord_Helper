const express = require('express');
const path = require('path');
const app = express();
const port = 3000
const { spawn } = require('child_process'); //spawn function from child_process module
const fs = require('fs');
const readline = require('readline');
const filePath = 'deleted_messages.txt';
let lastReadPosition = 0;

app.use(express.urlencoded({ extended: true}))
app.use(express.static('frontend'));

app.get("/",(req,res)=>{
    res.sendFile(path.join(__dirname, "/frontend/connect.html"));
})

app.post("/delete",(req,res)=>{
    const { token, channel} = req.body;
    console.log(token,channel)
    const python_process = spawn('python',['backend/DiscordApp.py',token, channel]);
    
    python_process.stdout.on('data', (data)=>{
        const message = data.toString();
        console.log(message);
    });
    
    python_process.on('error', (error) => {
        console.error(`Error: ${error.message}`);
    });
    
    python_process.on('close', (code) => {
    console.log(`Child process exited with code ${code}`);
    });
});

app.get("/messages", (req,res) => {
    //read .txt file and create array of lines
    //send array of lines
    const fileStream = fs.createReadStream(filePath,{ start: lastReadPosition, encoding: 'utf8' } )

    const rl = readline.createInterface({
        input:  fileStream,
        crlfDelay:Infinity,
    });

    const lines = []

    rl.on('line', (line) => {
        lines.push(line);
    });

    rl.on('close',()=>{
        lastReadPosition = fs.statSync(filePath).size;
        res.send(lines)
    });
    // fs.readFile('deleted_messages.txt', 'utf8', (err,data)=>{
    //     res.send(data);
    // })
});

app.listen(port, (error)=>{
    console.log("Listening on port: "+ port)
    if(error){
        console.log("something went wrong");
    }else{
        console.log("Server is listening on port " + port)
    }
})