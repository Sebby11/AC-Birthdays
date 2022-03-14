const alertTimeouts = {}

function showAlert(element, message, color, icon_class = null, seconds = 10000) {
    clearAlert(element);
    if (icon_class != null) {
        element.children[0].classList.add("fas", "pr-4");
        DOMTokenList.prototype.add.apply(element.children[0].classList, icon_class);
    }
    element.children[1].innerHTML = message;
    element.hidden = false;
    clearTimeout(alertTimeouts[element]);
    currTimeout = setTimeout(function () {
        clearAlert(element);
    }, seconds);
    alertTimeouts[element] = currTimeout;
}

function clearAlert(element) {
    clearTimeout(alertTimeouts[element]);
    element.hidden = true;
}
