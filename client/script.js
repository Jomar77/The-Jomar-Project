
const areaInput = document.getElementById('area');
const bedroomInput = document.getElementById('bedrooms');
const bathroomInput = document.getElementById('bathrooms');
const locationInput = document.getElementById('uiLocation');
const outputText = document.getElementById('output-field');

// Define variables for calculations
let area = 0;
let bedroom = 0;
let locat = '';
let bathroom = 0;

function onPageLoad() {
  console.log("Page loaded");
  var url = "http://localhost:5000/get_location_names";
  $.get(url, function (data, status) {
    console.log("got response for get_location_names request");
    if (data) {
      var locations = data.locations;
      var uiLocation = document.getElementById("uiLocation");
      $('#uiLocation').empty();
      for (var i in locations) {
        var opt = new Option(locations[i]);
        $('#uiLocation').append(opt);
      }
    }
    console.log(status);
  });
}




// Function to validate input values
function validateInput(event) {
  let inputField = event.target;
  let inputValue = inputField.value;

  // Set minimum and maximum input values based on input field
  let min = 0;
  let max = 0;
  switch (inputField.id) {
    case 'area':
      min = 100;
      break;
    case 'bedrooms':
    case 'bathrooms':
      min = 1;
      max = 5;
      break;
  }

  // Remove any non-numeric characters from the input value
  inputValue = inputValue.replace(/\D/g, '');

  // Set the input value to the minimum or maximum allowed value
  if (inputValue < min) {
    inputValue = min;
  } else if (max && inputValue > max) {
    inputValue = max;
  }

  // Update the input field value
  inputField.value = inputValue;
}


// Function to update output text
function updateOutput() {

  var url = "http://localhost:5000/predict_home_price";

  $.post(url, {
    location: locat,
    bathroom: bathroom,
    room: bedroom,
    area: area
  }, function (data, status) {
    console.log(data.estimated_price);
    outputText.textContent = `€${data.estimated_price}`;
    console.log(status);
  });

}

// Event listeners for inputs
areaInput.addEventListener('input',  validateInput, (e) => {
  area = parseInt(e.target.value) || 0;
  updateOutput();
});

bedroomInput.addEventListener('input', validateInput, (e) => {
  bedroom = parseInt(e.target.value) || 0;
  updateOutput();
});

bathroomInput.addEventListener('input', validateInput, (e) => {
  bathroom = parseInt(e.target.value) || 0;
  updateOutput();
});

locationInput.addEventListener('change', (e) => {
  locat = e.target.value;
  updateOutput();
});

window.onload = onPageLoad;