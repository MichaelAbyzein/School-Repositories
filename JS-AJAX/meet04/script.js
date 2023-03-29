document.addEventListener("DOMContentLoaded", () => {

    const key = "0e399381e397cdb8ac45192cef00241e";

    document.getElementById("submit-btn").onclick = function() {

        const request = new XMLHttpRequest;
        request.onload = function () {
            const data = JSON.parse(this.responseText);
            let ulElement = document.createElement("ul");
            Object.keys(data.rates).forEach(key => {
                const listItem = document.createElement("li");
                listItem.innerHTML = `${key} : ${data.rates[key]}`;
                ulElement.append(listItem);
            });

            document.querySelector(".content-result").append(ulElement);
        }
        request.open("GET", `http://data.fixer.io/api/latest?access_key=${key}`);
        request.send();

        return false;

    }
})