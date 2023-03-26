const headerSelect = document.getElementById('header-select');
const trainButton = document.getElementById('train-button');

const successMessage = document.getElementById('success-message');
const predictButton = document.getElementById('predict-button');

trainButton.addEventListener('click', function() {
    const selectedOptions = Array.from(headerSelect.selectedOptions).map(option => option.value);
    console.log('Selected Headers:', selectedOptions);
    // Perform the training with the selected headers
     // Send the selected headers to the server using an AJAX request
fetch('/train_model/', {
method: 'POST',
headers: {
  'Content-Type': 'application/json',
  'X-CSRFToken': document.querySelector('input[name="csrfmiddlewaretoken"]').value
},
body: JSON.stringify({ 'selected_headers': selectedOptions })
})
.then(response => response.json())
.then(data => {
// Handle the response from the server
console.log(data.message);
console.log('Mean Squared Error:', data.mse);
successMessage.style.display = 'block';
predictButton.style.display = 'inline-block';
});
predictButton.addEventListener('click', function() {
window.location.href = 'predict.html'; 
});

    // You can use AJAX or redirect the user to another view with the selected headers as parameters
});
