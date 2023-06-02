// Fonction pour récupérer les données à partir de l'API et les afficher dans le tableau HTML
function fetchData(url, tableId) {
  fetch(url)
    .then(response => response.json())
    .then(data => {
      const tableBody = document.getElementById(tableId);

      // Réinitialiser la table avant de la mettre à jour avec les nouvelles données
      tableBody.innerHTML = "";

      // Parcourir les données et les ajouter au tableau
      data.forEach(entry => {
        const row = document.createElement("tr");
        const idCell = document.createElement("td");
        const valueCell = document.createElement("td");

        idCell.textContent = entry[0];
        valueCell.textContent = entry[1];

        row.appendChild(idCell);
        row.appendChild(valueCell);

        tableBody.appendChild(row);
      });
    })
    .catch(error => console.error(error));
}

// Appeler la fonction fetchData pour chaque page HTML correspondante
function showTemperature() {
  fetchData("/realtime/temperature", "temperatureTable");
}

function showHumidity() {
  fetchData("/realtime/humidity", "humidityTable");
}

function showPressure() {
  fetchData("/realtime/pressure", "pressureTable");
}

