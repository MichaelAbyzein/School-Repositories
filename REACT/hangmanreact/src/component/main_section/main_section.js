import "./main_section.css"
import React, {useState, useEffect} from "react"

export default function MainSection(props){

    // const [status, setStatus] = React.useState(true);
    
    const [state, setState] = useState({
        words : [
                    "bear", 
                    "lion", 
                    "mouse", 
                    "tiger", 
                    "panther", 
                    "shark", 
                    "monkey", 
                    "buffalo", 
                    "llama", 
                    "whale", 
                    "rabbit",
                    "zebra",
                    "donkey",
                    "horse",
                    "penguin",
                    "panda",
                    "elephant",
                    "kiwi",
                    "squid",
                    "octopus"
        ],
        manstate : [
            "https://cdn.discordapp.com/attachments/586122410613276681/1086974923945287730/hangmanempty.png",
            "https://cdn.discordapp.com/attachments/586122410613276681/1086974924196954182/hangman0.png",
            "https://cdn.discordapp.com/attachments/586122410613276681/1086974924465381446/hangman1.png",
            "https://cdn.discordapp.com/attachments/586122410613276681/1086974924738002964/hangman2.png",
            "https://cdn.discordapp.com/attachments/586122410613276681/1086974925006454854/hangman3.png",
            "https://cdn.discordapp.com/attachments/586122410613276681/1086974925291659354/hangman4.png",
            "https://cdn.discordapp.com/attachments/586122410613276681/1086974925522337812/hangman5.png",
            "https://cdn.discordapp.com/attachments/586122410613276681/1086974923207090206/hangman6.png",
            "https://cdn.discordapp.com/attachments/586122410613276681/1086974923693637762/hangman7.png"
        ],
        manstateindex : 0,
        respondArray : ["Your guess is correct!", "Whoops! That's incorrect!", "You Failed!", "You Win!", "Please put a valid response!"],
        respondText : "Go on, start guessing!",
        word : [],
        remainingLetters : "",
        attemptarray : [],
        answerarray : "",
        guess : "",
        chances : 7,
        vissible : "block",
    });

    function choseRandomWord(word) {
        return word[Math.floor(Math.random() * word.length)]
    }

    function reject(currentchance, manindex){
        currentchance = currentchance - 1;
        manindex = manindex + 1;
        if (state.chances < 1){
            setState({
                ...state,
                guess : "",
                respondText : state.respondArray[2] + ` The correct answer is ${state.word.toUpperCase()}.`,
                manstateindex : manindex,
                vissible : "none",
            })
        } else {
            setState({
                ...state,
                guess : "",
                respondText : state.respondArray[1],
                chances : currentchance,
                manstateindex : manindex,
            })
        }
    }

    function calculateLength(word){
        return word.length
    }

    function validate(word, amount, response, array){
        for (var i in word) {
            if (word[i].includes(response)){
                amount = amount - 1;
                array[i] = " " + response + " ";
                if (amount === 0) {
                    setState({
                        ...state,
                        guess : "",
                        respondText : state.respondArray[3],
                        remainingLetters : amount,
                        vissible : "none",
                    })
                } else {
                    setState({
                        ...state,
                        guess : "",
                        respondText : state.respondArray[0],
                        remainingLetters : amount,
                    })
                }
            }
        } 
    }

    function startSession(){
        const word = choseRandomWord(state.words);
        const length = calculateLength(word);
        const array = setupAnswer(word);

        setState({
            ...state,
            word : word,
            remainingLetters : length,
            attemptarray : array,
        })
        return [word, length, array]

    }

    function updateResponse(event){
        setState({
            ...state,
            guess : event.target.value
        })
    }

    function setupAnswer(word) {
        let temparray = [];
        for (var i=0; i < word.length; i++){
            temparray[i] = " _ ";
        }
        return temparray;
    }
    
    function inputcheckResponse(event) {

        let response = state.guess.toUpperCase();
        let locword = state.word.toUpperCase().split("");
        let locarray = state.attemptarray;
        let locremain = state.remainingLetters;
        let newchances = state.chances;
        let manindex = state.manstateindex;

        if (event.key === "Enter") {

            let respondValid = locword.includes(response);

            if (respondValid === true) {

                validate(locword, locremain, response, locarray); 
            } else {

                reject(newchances, manindex)

            }

        }

    }

    function buttoncheckResponse(){

        let response = state.guess.toUpperCase()
        let locword = state.word.toUpperCase().split("")
        let locarray = state.attemptarray
        let locremain = state.remainingLetters
        let newchances = state.chances;
        let manindex = state.manstateindex;
        
        let respondValid = locword.includes(response);

        if (respondValid === true) {

            validate(locword, locremain, response, locarray);

        } else {

            reject(newchances, manindex)

        }

    }

    useEffect(() => {
        startSession();
    }, [])

    return (
        <div className="container">
            <h2>A React Hangman</h2>
            <br></br>
            <img src={state.manstate[state.manstateindex]}></img>
            <br></br>
            <h1>{state.attemptarray}</h1>
            <br></br>
            <input
                style={{
                    'display' : state.vissible
                }} 
                type="text" 
                value={state.guess}
                placeholder="" 
                onChange={updateResponse} 
                onKeyPress={inputcheckResponse}
            />
            <br></br>
            <button onClick={buttoncheckResponse} style={{ 'display' : state.vissible }}>Submit</button>
            <br></br>
            <p>Number of Chances Left : {state.chances}</p>
            <br></br>
            <p>Comment : {state.respondText}</p>
        </div>
    )

}