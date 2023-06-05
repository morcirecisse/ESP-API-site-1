          // Créer un objet de type Chart
          var ctx = document.getElementById('myChart').getContext('2d');
          var chart = new Chart(ctx, {
            type: 'line',
            data: {
              labels: [],
              datasets: [{
                label: 'temperature',
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: []
              },
              {
                label: 'Humidity',
                backgroundColor: 'rgb(153, 102, 255)',
                borderColor: 'rgb(153, 102, 255)',
                data: []
              },
            {
              label: 'Pressure',
                backgroundColor: 'rgb(183, 204, 248, 0.717)',
                borderColor: 'rgb(183, 204, 248, 0.717)',
                data: []
            }]
            },
            options: {}
          });
                   // Ajouter des données toutes les 3 secondes

                   $(document).ready(function(){
   setInterval(function() {
        $.get("http://localhost:5000/realtime", function(data) {
            var x = new Date();
            var y1 = parseFloat(data["degre"]);
            var y2 = parseFloat(data["taux_humidite"]);
            var y3 = parseFloat(data["hPa"]);
            chart.data.labels.push(x.toLocaleTimeString());
            chart.data.datasets[0].data.push(y1);
            chart.data.datasets[1].data.push(y2);
            chart.data.datasets[2].data.push(y3);
            chart.update();
        });
    }, 3000);
});