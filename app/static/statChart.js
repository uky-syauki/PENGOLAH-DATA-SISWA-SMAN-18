var xValues = GrafikData[0];
var yValues = GrafikData[1];

new Chart("myChart", {
	type: "bar",
	data: {
		labels: xValues,
		datasets: [{
			label: "Statistik penjualan",
			fill: false,
			lineTension: 0,
			backgroundColor: "rgba(0,0,255,1.0)",
			borderColor: "rgba(0,0,255,0.1)",
			data: yValues
		}]
	},
	options: {
/*		legend: {display: false}, */
		indexAxis: 'y',
		scales: {
			yAxes: [{ticks: {min: 0, max: 30}}],
		}
	}
});

document.getElementById("bulanInfo").innerText = bulan[0];
let total = 0;
yValues.forEach({} = x => total += x)
document.getElementById("totalInfo").innerText = total;

let getData = (bl) => {return bl.reduce((bagian, a) => bagian + a, 0)};
let sumData = [getData(tahun[0][0][1]), getData(tahun[0][1][1]), getData(tahun[0][2][1]), getData(tahun[0][3][1]), getData(tahun[0][4][1]), getData(tahun[0][5][1]), getData(tahun[0][6][1]), getData(tahun[0][7][1]), getData(tahun[0][8][1]), getData(tahun[0][9][1]), getData(tahun[0][10][1]), getData(tahun[0][11][1])];
let daftarBulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'];

new Chart(document.getElementById("horizontalBar"), {
    "type": "horizontalBar",
    "data": {
      "labels": daftarBulan,
      "datasets": [{
        "label": "My First Dataset",
        "data": sumData,
        "fill": false,
        "backgroundColor": ["rgba(255, 99, 132, 0.2)", "rgba(255, 159, 64, 0.2)",
          "rgba(255, 205, 86, 0.2)", "rgba(75, 192, 192, 0.2)", "rgba(54, 162, 235, 0.2)",
          "rgba(153, 102, 255, 0.2)", "rgba(201, 203, 207, 0.2)"
        ],
        "borderColor": ["rgb(255, 99, 132)", "rgb(255, 159, 64)", "rgb(255, 205, 86)",
          "rgb(75, 192, 192)", "rgb(54, 162, 235)", "rgb(153, 102, 255)", "rgb(201, 203, 207)"
        ],
        "borderWidth": 1
      }]
    },
    "options": {
      "scales": {
        "xAxes": [{
          "ticks": {
		max: 70,
            "beginAtZero": true
          }
        }]
      }
    }
  });



//bar
var ctxB = document.getElementById("barChart").getContext('2d');
var myBarChart = new Chart(ctxB, {
  type: 'bar',
  data: {
    labels: xValues, //["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
    datasets: [{
      label: '# of Votes',
      data: yValues, //[12, 19, 3, 5, 2, 3],
      backgroundColor: [
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)'
      ],
      borderColor: [
        'rgba(255,99,132,1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)'
      ],
      borderWidth: 1
    }]
  },
  options: {
    scales: {
	yAxes: [{ticks: {min: 0, max: 30}}],
	}
/*
      yAxes: [{
        ticks: {
          beginAtZero: true
        }
      }] *
    } */
  }
});


//line
/*
let tahun = tahun[0]

var ctxL = document.getElementById("lineChart").getContext('2d');
var myLineChart = new Chart(ctxL, {
  type: 'line',
  data: {
    labels: ["January", "February", "March", "April", "May", "June", "July"],
    datasets: [{
      label: "My First dataset",
      data: [65, 59, 80, 81, 56, 55, 40],
      backgroundColor: [
        'rgba(105, 0, 132, .2)',
      ],
      borderColor: [
        'rgba(200, 99, 132, .7)',
      ],
      borderWidth: 2
    },
    {
      label: "My Second dataset",
      data: [28, 48, 40, 19, 86, 27, 90],
      backgroundColor: [
        'rgba(0, 137, 132, .2)',
      ],
      borderColor: [
        'rgba(0, 10, 130, .7)',
      ],
      borderWidth: 2
    }
    ]
  },
  options: {
    responsive: true
  }
});
*/


let Januari = tahun[0][0][1]
let Februari = tahun[0][1][1]
let Maret = tahun[0][2][1]
let April = tahun[0][3][1]
let Mei = tahun[0][4][1]
let Juni = tahun[0][5][1]
let Juli = tahun[0][6][1]
let Agustus = tahun[0][7][1]
let September = tahun[0][8][1]
let Oktober = tahun[0][9][1]
let November = tahun[0][10][1]
let Desember = tahun[0][11][1]
        

        //line
var ctxL = document.getElementById("lineChart").getContext('2d');
var myLineChart = new Chart(ctxL, {
  type: 'line',
  data: {
  labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
    datasets: [
        

        {
        label: "Januari",
      data: Januari,
      backgroundColor: [
        'rgba(197, 72, 220, .2)',
      ],
      borderColor: [
        'rgba(8, 147, 83, .7)',
      ],
      borderWidth: 2
      },
        

        {
        label: "Februari",
      data: Februari,
      backgroundColor: [
        'rgba(66, 23, 236, .2)',
      ],
      borderColor: [
        'rgba(165, 116, 253, .7)',
      ],
      borderWidth: 2
      },
        

        {
        label: "Maret",
      data: Maret,
      backgroundColor: [
        'rgba(60, 145, 42, .2)',
      ],
      borderColor: [
        'rgba(116, 30, 11, .7)',
      ],
      borderWidth: 2
      },
        

        {
        label: "April",
      data: April,
      backgroundColor: [
        'rgba(102, 198, 224, .2)',
      ],
      borderColor: [
        'rgba(14, 84, 132, .7)',
      ],
      borderWidth: 2
      },
        

        {
        label: "Mei",
      data: Mei,
      backgroundColor: [
        'rgba(203, 248, 16, .2)',
      ],
      borderColor: [
        'rgba(255, 211, 149, .7)',
      ],
      borderWidth: 2
      },
        

        {
        label: "Juni",
      data: Juni,
      backgroundColor: [
        'rgba(27, 132, 214, .2)',
      ],
      borderColor: [
        'rgba(40, 28, 22, .7)',
      ],
      borderWidth: 2
      },
        

        {
        label: "Juli",
      data: Juli,
      backgroundColor: [
        'rgba(62, 143, 4, .2)',
      ],
      borderColor: [
        'rgba(243, 216, 239, .7)',
      ],
      borderWidth: 2
      },
        

        {
        label: "Agustus",
      data: Agustus,
      backgroundColor: [
        'rgba(248, 21, 10, .2)',
      ],
      borderColor: [
        'rgba(5, 17, 238, .7)',
      ],
      borderWidth: 2
      },
        

        {
        label: "September",
      data: September,
      backgroundColor: [
        'rgba(244, 62, 43, .2)',
      ],
      borderColor: [
        'rgba(229, 207, 38, .7)',
      ],
      borderWidth: 2
      },
        

        {
        label: "Oktober",
      data: Oktober,
      backgroundColor: [
        'rgba(47, 208, 134, .2)',
      ],
      borderColor: [
        'rgba(83, 146, 174, .7)',
      ],
      borderWidth: 2
      },
        

        {
        label: "November",
      data: November,
      backgroundColor: [
        'rgba(248, 104, 49, .2)',
      ],
      borderColor: [
        'rgba(74, 97, 248, .7)',
      ],
      borderWidth: 2
      },
        

        {
        label: "Desember",
      data: Desember,
      backgroundColor: [
        'rgba(203, 205, 40, .2)',
      ],
      borderColor: [
        'rgba(94, 108, 204, .7)',
      ],
      borderWidth: 2
      },
        

        ]
  },
  options: {
    responsive: true
  }
});

tr = document.getElementsByClassName("table")[1].getElementsByTagName("tr");
tr[tr.length-1].style.color = "blue";

