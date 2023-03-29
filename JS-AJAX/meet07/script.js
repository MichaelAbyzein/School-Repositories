document.addEventListener("DOMContentLoaded", () => {

    function createTable(tag) {
        let tablecontainer = document.querySelector(".table-container");
        let table = document.createElement("table");
        table.className = tag;
        tablecontainer.append(table);
    };

    function insertTableData(x, title, tabletag) {
        let xkey = x;
        let keyrow = document.createElement("tr");
        let keytitle = document.createElement("th");
        let keydata = document.createElement("th");
        keydata.innerHTML = x;
        keytitle.innerHTML = title;
        keyrow.append(keytitle);
        keyrow.append(keydata);
        document.querySelector(tabletag).append(keyrow);
    };

    function insertMultipleTableData(x, tabletag) {
        let xkey = Object.keys(x);
        xkey.forEach(key => {
            let keyrow = document.createElement("tr");
            let keytitle = document.createElement("th");
            let keydata = document.createElement("th");
            keytitle.innerHTML = key;
            keydata.innerHTML = x[key];
            keyrow.append(keytitle);
            keyrow.append(keydata);
            document.querySelector(tabletag).append(keyrow);
        });
    };

    document.getElementById("check-btn").addEventListener("click", () => {

        const request = new XMLHttpRequest();
        
        request.onload = function () {
            const sun = document.querySelector(".sun");
            const earthorbit = document.querySelector(".earth-orbit");
            const earth = document.querySelector(".earth");
            const btn = document.getElementById("check-btn");
            const percentcount = document.querySelector(".percent-count");

            var count = 0;
            percentcount.innerHTML = `${count}%`;

            sun.style.display = 'block';
            earthorbit.style.display = 'block';
            earth.style.display = 'block';
            percentcount.style.display = 'block';
            btn.style.display = 'none';
            

            const data = JSON.parse(this.responseText);

            createTable("table");
            let table = document.querySelector(".table");
            table.style.display = 'none';

            function counting() {
                ++count;
                percentcount.innerHTML = `${count}%`;

                if (count  == 100) {
                    clearInterval(countInterval);
                    sun.style.display = 'none';
                    earthorbit.style.display = 'none';
                    earth.style.display = 'none';
                    percentcount.style.display = 'none';

                    insertTableData(data.name, "name", ".table");
                    insertTableData(data.id, "id", ".table");
                    insertTableData(data.timezone, "timezone", ".table");

                    insertMultipleTableData(data.coord, ".table");
                    insertMultipleTableData(data.weather, ".table");
                    insertMultipleTableData(data.main, ".table");

                    table.style.display = 'block';
        
                }
            };


            

            let countInterval = setInterval(counting, 100);
            

        }
        request.open("GET", "http://127.0.0.1:5000/api/latest/weather");
        request.send();

    });
})