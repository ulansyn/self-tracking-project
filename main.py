from flask import Flask, render_template
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Data
data = {
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
}

@app.route('/')
def home():
    # Extracting dates and values from the data
    dates = list(data.keys())
    values = list(data.values())

    # Creating the plot
    plt.figure(figsize=(10, 6))
    plt.plot(dates, values, marker='o', linestyle='-', color='b')

    # Formatting the plot
    plt.title("Weight Over Time", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Weight (kg)", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.grid(True)

    # Ensure the 'static' folder exists
    if not os.path.exists('static'):
        os.makedirs('static')

    # Saving the plot to the static folder
    plot_path = 'static/weight_plot.png'
    plt.tight_layout()
    plt.savefig(plot_path)
    plt.close()

    return render_template('index.html', plot_path=plot_path)

if __name__ == '__main__':
    app.run(debug=True)
