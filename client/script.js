
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
  $.get(url, function(data, status) {
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



function limitInput(event) {
  const max = 5;
  const inputField = event.target;
  let inputValue = inputField.value;
  
  // Remove any non-numeric characters from the input value
  inputValue = inputValue.replace(/\D/g, '');
  
  // Limit the input value to the maximum allowed value
  if (inputValue > max) {
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
  }, function(data, status) {
    console.log(data.estimated_price);
    outputText.textContent = `$${data.estimated_price}`;
    console.log(status);
  });

}

// Event listeners for inputs
areaInput.addEventListener('input', (e) => {
  area = parseInt(e.target.value) || 0;
  updateOutput();
});

bedroomInput.addEventListener('input', limitInput, (e) => {
  bedroom = parseInt(e.target.value) || 0;
  updateOutput();
});

bathroomInput.addEventListener('input', limitInput, (e) => {
  bathroom = parseInt(e.target.value) || 0;
  updateOutput();
});

locationInput.addEventListener('change', (e) => {
  locat = e.target.value;
  updateOutput();
});

window.onload = onPageLoad;