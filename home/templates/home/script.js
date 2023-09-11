function addLoan() {
    document.querySelector("#formLoan").innerHtml = `
        <label>> Loan Name: </label>
        <input type="text" name="name" placeholder="House Loan" required> 
        <br>
        <label>> Priciple Amount: </label>
        <input type="number" name="priciple" placeholder="100000" min="5000" max="100000000" required> 
        <br>
        <label>> Interest Rate: </label>
        <input type="number" name="interest" placeholder="11.59" step="0.1" min="5" max="30" required> 
        <br>
        <label>> Tenure (In no of Months): </label>
        <input type="number" name="tenure" placeholder="24" min="6" max="500"required> 
        <br>
        <label>> Monthly EMI: </label>
        <input type="number" name="emi" placeholder="2000" min="100" max="1000000" required> 
        <br>
        <label>> Starting Month / Year: </label>
        <input type="month" name="start" required> 
        <br>
        <label>> Ending Month / Year: </label>
        <input type="month" name="end" required> 
        <br>
        <input type="submit" name="submit" value="Submit" required>
        `
}
document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("#loan").onclick = addLoan;
    document.querySelector("#expenses").onclick = addExpenses;
    document.querySelector("#investments").onclick = addInvestments;
})

