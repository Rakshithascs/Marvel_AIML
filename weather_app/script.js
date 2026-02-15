const apiKey = "7f69ea2475e10932854cb29f4e5cdad8";

function getWeather() {
    const city = document.getElementById("cityInput").value;

    fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("weatherResult").innerHTML = `
                <h3>${data.name}, ${data.sys.country}</h3>
                <p>Temperature: ${data.main.temp} °C</p>
                <p>Humidity: ${data.main.humidity}%</p>
                <p>Weather: ${data.weather[0].main}</p>
                <p>Description: ${data.weather[0].description}</p>
            `;
        })
        .catch(error => {
            document.getElementById("weatherResult").innerHTML = `<p>City not found!</p>`;
        });
}