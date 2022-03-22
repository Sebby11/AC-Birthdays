// Get div for data
const dataDiv = document.getElementById("data")

// Get DOM elements for birthday submission
const bdaySub = document.querySelector('.submit')
const bdayContainer = document.getElementById('birthday');

// Get Alert DOM elements
const article_alert = document.getElementById("article-alert");
article_alert.hidden = true;

// CREATE DOM elements for displaying character data
const dataTitle = document.createElement("p");
const dataImg = document.createElement("img");

//dataTitle.innerText = "AYO WHATS GOOD";
dataTitle.style.color = 'black';
//dataImg.src = "https://kitchenfunwithmy3sons.com/wp-content/uploads/2020/02/fluffy-cow-1-scaled.jpg"
dataImg.width = 200;
dataImg.height = 200;


dataDiv.appendChild(dataTitle);
dataDiv.appendChild(dataImg);
dataTitle.hidden = true;
dataImg.hidden = true;