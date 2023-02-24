// Select DOM elements
const areaInput = document.getElementById('area-input');
const bedroomInput = document.getElementById('bedroom-input');
const bathroomInput = document.getElementById('bathroom-input');
const locationInput = document.getElementById('location-input');
const outputText = document.getElementById('output-text');
const submitBtn = document.getElementById('calculate-btn');

// Define variables for calculations
let area = 0;
let bedroom = 0;
let bathroom = 0;
let location = '';

// Function to update output text
function updateOutput() {
  let price = calculatePrice(area, bedroom, bathroom, location);
  outputText.textContent = `$${price.toLocaleString()}`;
}

// Function to handle submit button click
function submitForm() {
  area = parseInt(areaInput.value) || 0;
  bedroom = parseInt(bedroomInput.value) || 0;
  bathroom = parseInt(bathroomInput.value) || 0;
  location = locationInput.value;
  updateOutput();
}

// Event listeners for inputs
areaInput.addEventListener('input', (e) => {
  area = parseInt(e.target.value) || 0;
  updateOutput();
});

bedroomInput.addEventListener('input', (e) => {
  bedroom = parseInt(e.target.value) || 0;
  updateOutput();
});

bathroomInput.addEventListener('input', (e) => {
  bathroom = parseInt(e.target.value) || 0;
  updateOutput();
});

locationInput.addEventListener('change', (e) => {
  location = e.target.value;
  updateOutput();
});

submitBtn.addEventListener('click', (e) => {
  e.preventDefault();
  submitForm();
});

// Function to calculate price
function calculatePrice(area, bedroom, bathroom, location) {
  let basePrice = 50000;
  let areaMultiplier = 1000;
  let bedroomMultiplier = 10000;
  let bathroomMultiplier = 5000;
  let locationMultiplier = 1;

  switch (location) {
    case 'New York':
      locationMultiplier = 1.5;
      break;
    case 'Los Angeles':
      locationMultiplier = 1.2;
      break;
    case 'San Francisco':
      locationMultiplier = 1.3;
      break;
    case 'Miami':
      locationMultiplier = 1.1;
      break;
  }

  let price = basePrice + area * areaMultiplier + bedroom * bedroomMultiplier + bathroom * bathroomMultiplier;
  price *= locationMultiplier;

  return price;
}
