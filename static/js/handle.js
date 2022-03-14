// Event trigger when birthday is entered
bdaySub.addEventListener('click', () => {
	if (bdayContainer.value == ''){
		console.log("Empty!");
	}
	else{
		console.log(bdayContainer.value);

		// Send data to flask backend to scrape from page
        fetch(`${window.origin}/parse-bday-data`, {
            method: "POST",
            credentials: "include",
            body: JSON.stringify(bdayContainer.value),
            cache: "no-cache",
            headers: new Headers({
                "content-type": "application/json",
            }),
        })
        .then(function (response) {
            if (response.status !== 200) {
                showAlert(article_alert, "Page could not be reached!", "red", [
                    "fa-exclamation-triangle",
                ]);
                return;
            }

            response.json().then(function (birthday_data) {
                console.log("DATA: ", birthday_data)
            });

        })
        .catch(function (error) {
            showAlert(article_alert, "Error in the backend... Please stand by!", "red", [
                "fa-exclamation-triangle",
            ]);
            console.log("Fetch error: " + error);
        });
	}
})