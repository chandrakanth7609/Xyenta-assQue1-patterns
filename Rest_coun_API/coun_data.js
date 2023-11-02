const countriesList = document.getElementById("countries-list");

// Fetch data from the REST Countries API
fetch("https://restcountries.com/v3.1/all")
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        // Loop through the countries data
        data.forEach(country => {
            const countryCard = document.createElement("div");
            countryCard.classList.add("country-card");

            // Display relevant information for each country
            countryCard.innerHTML = `
                <h2>${country.name?.common || "N/A"}</h2>
                <p>Population: ${country.population?.toLocaleString() || "N/A"}</p>
                <p>Languages: ${country.languages ? Object.values(country.languages).join(", ") : "N/A"}</p>
                <p>Currency: ${country.currencies ? (country.currencies[0]?.name || "N/A") + ` (${country.currencies[0]?.code || "N/A"})` : "N/A"}</p>
                <p>Timezones: ${country.timezones ? country.timezones.join(", ") : "N/A"}</p>
            `;

            countriesList.appendChild(countryCard);
        });
    })
    .catch(error => {
        console.error("Error fetching data:", error);
    });
