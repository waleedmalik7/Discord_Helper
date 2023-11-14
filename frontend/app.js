const token = document.querySelector("#token");
const chID = document.querySelector("#channel");
const submit = document.querySelector(".submit");
const result = document.querySelector('.result-container');
const wrapper = document.querySelector('.content-wrapper');

const addline = (content) =>{
    const line = document.createElement('div')
    line.innerText = content;
    line.setAttribute('class','return-text')
    result.append(line);
}

const postInfo = async () =>{
    const urlSearchParams = new URLSearchParams();

    // Add key-value pairs to the object
    urlSearchParams.append("token", token.value);
    urlSearchParams.append("channel", chID.value);
    
    // Make an asynchronous POST request using Fetch
    fetch("/delete", {
        method: "POST",
        body: urlSearchParams.toString(),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
}

const getInfo = async () =>{
    return fetch("/messages").then((response)=>{
        return response.text();
    });
}   

submit.addEventListener("click", async(e) =>{
    e.preventDefault();
    wrapper.style.display = 'block';
    await postInfo(); 
    setInterval(() => {
        getInfo().then((data)=>{
            formatted_data = data.split('\n');
            console.log(formatted_data);
            formatted_data.forEach(line => {
                addline(line);
            });
        });
        console.log('-------------------');
    }, 5000);
})