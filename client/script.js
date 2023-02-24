const inputForm = document.getElementById('input-form');
const outputContainer = document.getElementById('output-container');
const outputField = document.getElementById('output-field');

inputForm.addEventListener('submit', (event) => {
  event.preventDefault();

  gsap.to('#input-section', {opacity: 0, duration: 0.5, onComplete: () => {
    outputContainer.classList.add('fade-in');
    gsap.to('#output-section', {opacity: 1, duration: 0.5});
  }});

  outputField.innerText = '$500,000';
});