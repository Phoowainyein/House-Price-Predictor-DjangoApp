document.getElementById("file-upload").addEventListener("change", function() {
    // Code to execute when a file is selected
    // For this case , will hide the button:
    const selectFileButton = document.querySelector("label[for='file-upload']");
selectFileButton.classList.add("hidden");
// Change the "Upload your file" text to "Submit your file" when a file is selected
const uploadText = document.querySelector(".title p");
    uploadText.textContent = "Submit your file !";

// Change the submit button's background color and size when a file is selected
 const submitButton = document.querySelector("input[type='submit']");
 submitButton.classList.remove("hidden");
submitButton.style.backgroundColor = "#0d8907";
submitButton.style.fontSize = "1.2em";
submitButton.style.padding = "12px 24px";
submitButton.style.borderRadius = "5px";
// Change the submit button's hover background color
submitButton.style.transition = "background-color 0.5s ease-in-out";
submitButton.addEventListener("mouseover", function() {
submitButton.style.backgroundColor = "#1cd312";
});
submitButton.addEventListener("mouseout", function() {
submitButton.style.backgroundColor = "#0d8907";
});


    
});
document.querySelector('form').addEventListener('submit', function(e) {
e.preventDefault(); // prevent the form from submitting normally

const fileInput = document.querySelector('#file-upload');
const file = fileInput.files[0];
const allowedExtensions = /(\.csv)$/i; // regular expression to match CSV files
if (!allowedExtensions.exec(file.name)) {
alert('Please select a CSV file.');
fileInput.value = '';
return false;
}

// create a FormData object to send the file with the form data
const formData = new FormData();
formData.append('csv_file', document.querySelector('#file-upload').files[0]);

// send the form data to the server using an AJAX request
fetch('/upload_csv/', {
method: 'POST',
body: formData,
headers: {
'X-CSRFToken': document.querySelector('input[name="csrfmiddlewaretoken"]').value
}
}).then(response => {
if (response.ok) {
// check if the CSV file is valid
response.json().then(data => {
    if (data.is_valid) {
        // redirect to the train.html page if the upload was successful and the CSV file is valid
        window.location.href = "train.html";
    } else {
        // show the error message if the CSV file is invalid
        alert(data.error_message);
    }
});
} else {
alert('Upload failed.');
}
});

});
function highlightNav(element) {
var navLinks = document.querySelectorAll("#navbar a");
navLinks.forEach(function(link) {
    link.classList.remove("active");
});
element.classList.add("active");
}





