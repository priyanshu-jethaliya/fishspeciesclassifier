function predictSpecies() {
    const length = parseFloat(document.getElementById("length").value);
    const width = parseFloat(document.getElementById("width").value);
    const height = parseFloat(document.getElementById("height").value);
    const weight = parseFloat(document.getElementById("weight").value);

    // Show a loading message while waiting for the prediction
    const resultDiv = document.getElementById("predictionResult");
    resultDiv.innerText = "Predicting...";

    // Sending the input data to the backend for prediction
    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            length: length,
            width: width,
            height: height,
            weight: weight,
        }),
    })
    .then((response) => response.json())
    .then((data) => {
        resultDiv.innerText = `Predicted Fish Species: ${data.species}`;
    })
    .catch((error) => {
        resultDiv.innerText = "Error occurred. Please try again.";
        console.error("Error:", error);
    });
}
