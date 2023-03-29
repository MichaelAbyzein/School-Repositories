
// const request = new XMLHttpRequest();
// request.onload = function(){
//     const response = JSON.parse(this.responseText);
//     console.log(this.response);
// }

// request.open('GET', 'https://www.omdbapi.com/?t=Spongebob&apikey=b07d1ac2');
// request.send();

// fetch("https://www.omdbapi.com/?t=Spongebob&apikey=b07d1ac2")
//     .then(response => response.json())
//     .then(response => console.log(response));

// $.ajax({
//     url : "https://www.omdbapi.com/?t=Spongebob&apikey=b07d1ac2",
//     success : response => console.log(response)
// })

// const fulfilled = true;
// const promise = new Promise((resolve, reject)=>{
//     if(fulfilled){
//         resolve("Done!") // return fulfilled
//     } else {
//         reject("Nope.") // return not fulfilled
//     }
// });

// promise
//     .then(response => console.log("Okay! It's "+response))
//     .catch(response => console.log("Sorry, that's a "+response));

fetch("https://www.omdbapi.com/?t=Spongebob&apikey=b07d1ac2")
    .then(response => response.json())
    .then(response => console.log(response))
    .catch(response => console.log("Soory, I couldn't fetch your stuff!" + error));