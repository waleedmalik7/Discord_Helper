const token = document.querySelector("#token");
const chID = document.querySelector("#channel");
const submit = document.querySelector(".submit");
const baseUrl = 'http://localhost:3000/'

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

submit.addEventListener("click",(e)=>{
    //submit the form
    e.preventDefault();
    postInfo();
})