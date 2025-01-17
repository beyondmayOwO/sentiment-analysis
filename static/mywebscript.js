let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    // Create a new XMLHttpRequest object
    let xhttp = new XMLHttpRequest();

    // Define a callback function to handle the server response
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            // Update the HTML element with ID "system_response" with the server response
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
    };
    
    // Open a GET request to the server endpoint "sentimentAnalyzer" with the user input as a query parameter
    xhttp.open("GET", "sentimentAnalyzer?textToAnalyze"+"="+textToAnalyze, true);
    
    // Send the request
    xhttp.send();
}
