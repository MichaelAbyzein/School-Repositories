document.addEventListener("DOMContentLoaded", ()=> {

    let url = "https://www.omdbapi.com/?apikey=b07d1ac2&s=spongebob";

    function clearSearchSection(){
        try {
            const table = document.querySelector("table");
            table.innerHTML = "";
            return true;
        } catch(error) {
            console.log(error)
            return false
        }
    }

    function putLoading(){
        const table = document.querySelector("table");
        table.innerHTML = "Loading...";
    }

    function addMovietoResultSection(movies){
        const table = document.querySelector("table");
        movies.forEach(movie => {
            const row = document.createElement("tr");
            const title = document.createElement("td");
            title.append(movie.Title);
            const year = document.createElement("td");
            year.append(movie.Year);
            const imgPoster = document.createElement("img");
            imgPoster.src = movie.Poster;
            imgPoster.alt = movie.Title
            const poster = document.createElement("td");
            poster.append(imgPoster);

            row.append(title);
            row.append(year);
            row.append(poster);
            table.append(row);
        });
    }

    function getFilmwithErrorHandler(searchQuerry){
        const ajax = new XMLHttpRequest();
        ajax.onload = function(){
            clearSearchSection();
            putLoading();
            if (this.status === 200) {
                setTimeout(() => {
                    const response = JSON.parse(this.responseText);
                    console.log(response)
                    clearSearchSection();
                    addMovietoResultSection(response.Search);
                }, 2000)
            } else {
                clearSearchSection();
                console.log("Error get movies");
                alert("Error get movies!")
            }
            
        }

        // ajax.onreadystatechange = function(){
        //     if (this.readyState === 4 && this.status === 200){

        //     }
        // }

        ajax.open("GET", `${url+searchQuerry}`);
        ajax.send();
    }
    
    function getFilm(searchQuerry){
        const ajax = new XMLHttpRequest();
        ajax.onload = function(){
            clearSearchSection();
            putLoading();
            setTimeout(() => {
                const response = JSON.parse(this.responseText);
                console.log(response)
                clearSearchSection();
                addMovietoResultSection(response.Search);
            }, 2000)
            
        }

        ajax.open("GET", `${url+searchQuerry}`);
        ajax.send();
    }

    function getFilmwithJQuerry(searchQuerry){
        $.ajax({
            url : `${url+searchQuerry}`,
            success : (response) => {
                clearSearchSection();
                putLoading();
                setTimeout(() => {
                    console.log(response)
                    clearSearchSection();
                    addMovietoResultSection(response.Search);
                }, 2000)
            },
            error : (error) => {
                console.log("Error get movies!");
                alert(`Error get movies!${error.responseText}`)
            }
        })
            
    }

    document.querySelector("button").addEventListener("click", () => {
        const sQ = document.querySelector("#search-entry").value;
        // getFilm(sQ);
        getFilmwithErrorHandler(sQ);
        // getFilmwithJQuerry(sQ)
    })
   

})