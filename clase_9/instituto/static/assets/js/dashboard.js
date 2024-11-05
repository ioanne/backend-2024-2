$(function () {
// -----------------------------------------------------------------------
  // Traffic Overview
  // -----------------------------------------------------------------------

  var chart = {
    series: [
      {
        name: "New Users",
        data: [5, 1, 17, 6, 15, 9, 6],
      },
      {
        name: "Users",
        data: [7, 11, 4, 16, 10, 14, 10],
      },
    ],
    chart: {
      toolbar: {
        show: false,
      },
      type: "line",
      fontFamily: "inherit",
      foreColor: "#adb0bb",
      height: 320,
      stacked: false,
    },
    colors: ["var(--bs-gray-300)", "var(--bs-primary)"],
    plotOptions: {},
    dataLabels: {
      enabled: false,
    },
    legend: {
      show: false,
    },
    stroke: {
      width: 2,
      curve: "smooth",
      dashArray: [8, 0],
    },
    grid: {
      borderColor: "rgba(0,0,0,0.1)",
      strokeDashArray: 3,
      xaxis: {
        lines: {
          show: false,
        },
      },
    },
    yaxis: {
      title: {
        // text: 'Age',
      },
    },
    xaxis: {
      axisBorder: {
        show: false,
      },
      axisTicks: {
        show: false,
      },
      categories: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    },
    yaxis: {
      tickAmount: 4,
    },
    markers: {
      strokeColor: ["var(--bs-gray-300)", "var(--bs-primary)"],
      strokeWidth: 2,
    },
    tooltip: {
      theme: "dark",
    },
  };

  var chart = new ApexCharts(
    document.querySelector("#traffic-overview"),
    chart
  );
  chart.render();


})