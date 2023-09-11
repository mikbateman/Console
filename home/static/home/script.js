function addInvestements() {
    myStyles = `
    background-color: #1a1a1a;
    margin: 2px;
    border: solid 3px #808080;
    border-radius: 10px;
    padding: 10px;
    color: yellow;
    height: 230px;
    width: 600px;
    `;
    if (document.querySelector("#bi").innerHTML === "<strong>Add+</strong>") {
        document.querySelector("#bi").innerHTML = "<strong>Close</strong>";
        document.querySelector(".investments").style.cssText = myStyles;
        document.querySelector("#formInvestments").innerHTML = `
            <label>> Stocks:</label>
            <input type="number" name="stocks" min="100" max="1000000" required>
            <br>
            <label>> Mutual Funds:</label>
            <input type="number" name="mf" min="100" max="1000000" required>
            <br>
            <label>> Gold:</label>
            <input type="number" name="gold" min="100" max="1000000" required>
            <br>
            <label>> Other:</label>
            <input type="number" name="other" min="100" max="1000000" required>
            <br>
            <input type="submit" name="submit" value="Submit">

            `;
    }
    else {
        document.querySelector("#bi").innerHTML = "Add+";
        document.querySelector(".investments").style.cssText = ``;
        document.querySelector("#formInvestments").innerHTML = ``;

    }
}
function addExpenses() {
    myStyles = `
    background-color: #1a1a1a;
    margin: 2px;
    border: solid 3px #808080;
    border-radius: 10px;
    padding: 10px;
    color: yellow;
    height: 520px;
    width: 600px;
    `;
    if (document.querySelector("#be").innerHTML === "<strong>Add+</strong>") {
        document.querySelector("#be").innerHTML = "<strong>Close</strong>";
        document.querySelector(".expenses").style.cssText = myStyles;
        document.querySelector("#formExpenses").innerHTML = `
            <label>> Year:</label>
            <input type="number" name="year" min="1980" max="2200"required>
            <br>
            <label>> Month:</label>
            <input type="month" name="month" required>
            <br>
            <label>> Income:</label>
            <input type="number" name="income" min="100" max="1000000" required>
            <br>
            <label>> Utilities:</label>
            <input type="number" name="utilities" min="100" max="1000000" required>
            <br>
            <label>> Food:</label>
            <input type="number" name="food" min="100" max="1000000" required>
            <br>
            <label>> Entertainment:</label>
            <input type="number" name="entertainment" min="100" max="1000000" required>
            <br>
            <label>> Groceries:</label>
            <input type="number" name="groceries" min="100" max="1000000" required>
            <br>
            <label>> Subscriptions:</label>
            <input type="number" name="subscriptions" min="100" max="1000000" required>
            <br>
            <label>> EMIs:</label>
            <input type="number" name="emi" min="100" max="1000000" required>
            <br>
            <label>> Other:</label>
            <input type="number" name="other" min="100" max="1000000" required>
            <br>
            <input type="submit" name="submit" value="Submit">
            `
    }
    else {
        document.querySelector("#be").innerHTML = "<strong>Add+</strong>";
        document.querySelector(".expenses").style.cssText = ``;
        document.querySelector("#formExpenses").innerHTML = ``;

    }
}

function addLoan() {
    myStyles = `
    background-color: #1a1a1a;
    margin: 2px;
    border: solid 3px #808080;
    border-radius: 10px;
    padding: 10px;
    color: yellow;
    width: 500px;
    height: 380px;
    `;
    if (document.querySelector("#bl").innerHTML === "<strong>Add+</strong>") {
        document.querySelector("#bl").innerHTML = "<strong>Close</strong>";
        document.querySelector(".loan").style.cssText = myStyles;
        document.querySelector("#formLoan").innerHTML = `
            <label>> loan name: </label>
            <input type="text" name="name" placeholder="house loan" required> 
            <br>
            <label>> priciple amount: </label>
            <input type="number" name="priciple" placeholder="100000" min="5000" max="100000000" required> 
            <br>
            <label>> interest rate: </label>
            <input type="number" name="interest" placeholder="11.59" step="0.1" min="5" max="30" required> 
            <br>
            <label>> tenure (in no of months): </label>
            <input type="number" name="tenure" placeholder="24" min="6" max="500"required> 
            <br>
            <label>> monthly emi: </label>
            <input type="number" name="emi" placeholder="2000" min="100" max="1000000" required> 
            <br>
            <label>> starting month / year: </label>
            <input type="month" name="start" required> 
            <br>
            <label>> ending month / year: </label>
            <input type="month" name="end" required> 
            <br>
            <input type="submit" name="submit" value="submit" required>
            `
    }
    else {
        document.querySelector("#bl").innerHTML = "<strong>Add+</strong>";
        document.querySelector(".loan").style.cssText = ``;
        document.querySelector("#formLoan").innerHTML = ``;

    }
}
