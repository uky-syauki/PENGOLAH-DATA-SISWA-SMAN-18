var xValues = GrafikData[0];
var yValues = GrafikData[1];

new Chart("myChart", {
	type: "line",
	data: {
		labels: xValues,
		datasets: [{
			fill: false,
			lineTension: 0,
			backgroundColor: "rgba(0,0,255,1.0)",
			borderColor: "rgba(0,0,255,0.1)",
			data: yValues
		}]
	},
	options: {
		legend: {display: false},
		scales: {
			yAxes: [{ticks: {min: 0, max: 30}}],
		}
	}
});

document.getElementById("bulan").innerText = bulan[0]
