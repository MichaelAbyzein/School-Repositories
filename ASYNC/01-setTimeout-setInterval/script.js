document.addEventListener("DOMContentLoaded", ()=> {

    function consolelogdelay(number){
        setTimeout(() => {
            console.log(number)
        }, 2000)
    }

    console.log(1);
    // console.log(2);
    consolelogdelay(2);
    console.log(3);

    document.querySelector("#btn-stop-interval").addEventListener("click", ()=>{

    })

})