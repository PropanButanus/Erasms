odoo.define('custom_snippets.fetch_bitcoin', function (require) {
    'use strict';

    var ajax = require('web.ajax');
    var Chart = require('chartjs');

    $(document).ready(function () {
        var ctx = document.getElementById('bitcoin-chart').getContext('2d');

        var bitcoinChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: [],
                datasets: [{
                    label: 'Bitcoin Price',
                    data: [],
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    xAxes: [{
                        type: 'time',
                        time: {
                            unit: 'day'
                        }
                    }],
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                },
                beforeInit: function (chart) {
                    // Load more data when user scrolls or zooms in
                    chart.options.scales.xAxes[0].afterDataLimits = function (scale) {
                        var data = chart.data.datasets[0].data;
                        var lastDate = data[data.length - 1].x;
                        var nextDate = moment(lastDate).add(1, 'day').format('YYYY-MM-DD');
                        loadMoreData(nextDate, chart);
                    }
                }
            }
        });

        function loadMoreData(startDate, chart) {
            ajax.jsonRpc('/custom_snippets/get_bitcoin_data', 'json', {'start_date': startDate})
                .then(function (data) {
                    var bitcoinData = data['Close'];
                    chart.data.labels.push(...bitcoinData.index);
                    chart.data.datasets[0].data.push(...bitcoinData.values);
                    chart.update();
                });
        }
        return bitcoinChart;
    });
});
