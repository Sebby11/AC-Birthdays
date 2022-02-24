// Event trigger when birthday is entered
bdaySub.addEventListener('click', () => {
	if (bdayContainer.value == ''){
		console.log("Empty!");
	}
	else{
		console.log(bdayContainer.value);
	}
})