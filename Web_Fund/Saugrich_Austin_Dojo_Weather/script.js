// get rid of cookie pop up

function cookieBye() {
    document.querySelector('.cookie').style.display = 'none'

}


// function to change temp to far or cel

function toCel2() {

    var selectedUnit = document.getElementById("temp").value;
    var temperatureElements = document.getElementsByClassName("num");
    for (var i = 0; i < temperatureElements.length; i++) {
        var currentTemperature = parseInt(temperatureElements[i].innerText);
        if (selectedUnit === "far") {
            currentTemperature = (currentTemperature * 9 / 5) + 32;
        } else {
            currentTemperature = (currentTemperature - 32) * 5 / 9;
        }
        temperatureElements[i].innerHTML = Math.round(currentTemperature);
    }
}