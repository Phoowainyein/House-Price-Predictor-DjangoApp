// Get the predict button and result div elements
const predictButton = document.getElementById("predict-price");
const resultDiv = document.getElementById("result-div");
const errorMessageDiv = document.getElementById("error-message");

// Add a click event listener to the predict button
predictButton.addEventListener("click", () => {
  // Get the input values for zip code, square meters, acre size, number of bedrooms, and number of bathrooms
  const zipCode = document.getElementsByName("n1")[0].value;
  const squareMeters = document.getElementsByName("n2")[0].value;
  const acreSize = document.getElementsByName("n3")[0].value;
  const numBedrooms = document.getElementsByName("n4")[0].value;
  const numBathrooms = document.getElementsByName("n5")[0].value;

  // Check if any input field is empty
  if (!zipCode || !squareMeters || !acreSize || !numBedrooms || !numBathrooms) {
    errorMessageDiv.innerText = "Please fill in all input fields.";
    errorMessageDiv.style.display = "block";
    return;
  }

    // Check if zip code is at least 5 digits
    if (zipCode.length < 5) {
    errorMessageDiv.innerText = "Please enter a valid zip code with at least 5 digits.";
    errorMessageDiv.style.display = "block";
    return;
  }


    // Hide the error message if all input fields are filled in
    errorMessageDiv.style.display = "none";

  // Create a new XML HTTP request object
  const xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
      // Parse the JSON response
      const response = JSON.parse(this.responseText);
      // Display the response in the result div
      resultDiv.innerHTML = `<p style="color: green; background-color: gray;display: inline-block; padding: 10px; ">The predicted price is: $${response.predicted_price}</p>`;
    }
  };
  xhr.open("GET", `predict_model/?n1=${zipCode}&n2=${squareMeters}&n3=${acreSize}&n4=${numBedrooms}&n5=${numBathrooms}`);
  xhr.send();
});