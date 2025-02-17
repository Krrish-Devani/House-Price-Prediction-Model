document.getElementById("prediction-form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let formData = new FormData(this);
    
    fetch("/predict", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.prediction !== undefined) {  // Check if prediction exists
            document.getElementById("result").innerText = "Predicted Price: $" + data.prediction + "K";
        } else if (data.error) {  // Show error from Flask
            document.getElementById("result").innerText = "Error: " + data.error;
        } else {
            document.getElementById("result").innerText = "Error: Unexpected response";
        }
    });
});
