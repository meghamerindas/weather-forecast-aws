function getForecast() {
  const city = document.getElementById("city").value;
  const email = document.getElementById("email").value;

  
  if (!city || !email) {
    alert("❗ Please select a city and enter your email.");
    return;
  }

  
  fetch("https://kqqvzl5hbf.execute-api.ap-south-1.amazonaws.com/forecast", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      city: city,
      email: email
    })
  })
  .then(response => response.json())
  .then(data => {
    const resultDiv = document.getElementById("result");

    if (data.message) {
      resultDiv.innerHTML = `
        <p style="color: green;"><strong>✅ ${data.message}</strong></p>
        ${
          data.prediction
            ? `<p><strong>Predicted Temp:</strong> ${data.prediction[0]}°C</p>`
            : ""
        }
      `;
    } else if (data.error) {
      resultDiv.innerHTML = `
        <p style="color: red;"><strong>❌ ${data.error}</strong></p>
      `;
    }
  })
  .catch(error => {
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = `
      <p style="color: red;"><strong>❌ Error:</strong> ${error.message}</p>
    `;
    console.error("Fetch error:", error);
  });
}
