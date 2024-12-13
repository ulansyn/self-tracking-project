const data = {
    "31.10.2024": 72.1,
    "01.11.2024": 71.6,
    "02.11.2024": 72.1,
    "03.11.2024": 73.3,
    "04.11.2024": 72.5,
    "05.11.2024": 71.5,
    "06.11.2024": 71.5,
    "08.11.2024": 72.9,
    "11.11.2024": 72.9,
    "12.11.2024": 73.3,
    "14.11.2024": 74.4,
    "20.11.2024": 73.2,
    "22.11.2024": 73.3,
    "23.11.2024": 73.1,
    "24.11.2024": 73.3,
    "27.11.2024": 74.0,
    "30.11.2024": 74.7,
    "02.12.2024": 73.2,
    "04.12.2024": 73.4,
    "05.12.2024": 73.0,
    "09.12.2024": 73.6,
    "13.12.2024": 74.8
};

// Преобразуем даты и веса в массивы
const dates = Object.keys(data);
const weights = Object.values(data);

// График с использованием Chart.js
const ctx = document.getElementById('weightChart').getContext('2d');
const weightChart = new Chart(ctx, {
    type: 'line', // Линейный график
    data: {
        labels: dates,
        datasets: [{
            label: 'Вес (кг)',
            data: weights,
            borderColor: 'rgba(75, 192, 192, 1)',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            fill: true,
            tension: 0.4, // Интерполяция между точками
            pointRadius: 5, // Размер точек
            pointBackgroundColor: 'rgba(75, 192, 192, 1)'
        }]
    },
    options: {
        responsive: true,
        scales: {
            x: {
                type: 'category',
                title: {
                    display: true,
                    text: 'Дата'
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Вес (кг)'
                },
                beginAtZero: false
            }
        }
    }
});
