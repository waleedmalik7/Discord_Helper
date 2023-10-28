const http = require('http')
const port = 3000

const server = http.createServer((req, res)=>{
    
})

server.listen(port, (error)=>{
    console.log("Listening on port: "+ port)
    if(error){
        console.log("something went wrong");
    }else{
        console.log("Server is listening on port " + port)
    }
})