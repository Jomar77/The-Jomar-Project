async function getData(){

const response = await fetch('duo.json')
const data =  await response.json()
const {site_streak} = data
document.getElementById('myLink').textContent = site_streak;
}

window.onload = getData();