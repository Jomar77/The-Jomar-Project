async function getData(){

const response = await fetch('API/duo.json')
const data =  await response.json()
const {site_streak} = data
document.getElementById('myLink').textContent = site_streak;
}

window.onload = getData();