document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("check-btn").addEventListener("click", () => {
        const request = new XMLHttpRequest();

        request.onload = function () {
            const data = JSON.parse(this.responseText);
            keys = Object.keys(data.rates);
            keys.forEach(key => {
                // console.log(`${key} - ${data.rates[key]}`);
                const rates = document.createElement("td");
                const currency = document.createElement("td");
                const row = document.createElement("tr");
                rates.innerHTML = data.rates[key];
                currency.innerHTML = key;
                row.append(rates);
                row.append(currency);
                document.querySelector(".result").append(row)
                
            });

        }
        request.open("GET", "http://127.0.0.1:5000/api/latest/currency/latest");
        request.send();
    })
})