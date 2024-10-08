# Temperature Forecasting Time Series Project

## Project Overview

This project involves predicting long-term daily temperatures using time series forecasting techniques. We tested various statistical and deep learning models to estimate future temperatures, including:
- **ARIMA (AutoRegressive Integrated Moving Average)**
- **SARIMA (Seasonal AutoRegressive Integrated Moving Average)**
- **LSTM (Long Short-Term Memory networks)**
- **Prophet**

After testing these models, **Prophet** delivered the most accurate results. The project also includes a web-based deployment using **Flask** to interact with the Prophet model for forecasting.

## Models Tested

1. **ARIMA**: A statistical model for time series forecasting that incorporates autoregression, differencing, and moving averages.
   
2. **SARIMA**: An extension of ARIMA that supports seasonality in time series data.
   
3. **LSTM**: A deep learning model that captures long-term dependencies in sequential data, making it suitable for time series prediction.

4. **Prophet**: A model developed by Facebook that handles seasonality and holidays efficiently. It's known for ease of use and robustness with time series that have missing data or outliers.

## Best Model: Prophet
The **Prophet** model outperformed ARIMA, SARIMA, and LSTM, giving better results for long-term temperature forecasting. The Flask web app utilizes this model for real-time forecasting.

## Project Structure

```console
project-root/
│
├── arima-sarima_lstm/          # Folder containing ARIMA, SARIMA, and LSTM models
├── daily temperature-prophet/  # Folder containing Prophet model
├── DATA/                       # Folder with raw and preprocessed temperature datasets
├── static/                     # Static files (CSS, JS, images) for the web app
├── templates/                  # HTML templates for the web app
├── app.py                      # Main Flask application
├── .gitignore                  # Git ignore file
├── README.md                   # Project documentation ```
```

## Project Overview
In this project, we explored multiple statistical and deep learning models to forecast daily temperatures. The Prophet model outperformed others in accuracy and is used for the final deployment.

## Web Application

The Flask application serves a web-based interface where users can interact with the Prophet model and view future temperature forecasts. The app allows users to either upload a dataset or use the existing one for predictions.

### How It Works:
- The Flask app (`app.py`) runs the web server.
- It uses HTML templates stored in the `templates/` folder to render the user interface.
- Static files like CSS and JavaScript are stored in the `static/` folder.

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/ahmedcherif11/Cheetass_Pose_estimation-.git
cd project-root
```
### 2. Install Dependencies
### 3. Run the Flask App
Run the following command to start the Flask web server:

```bash
python app.py
```

Once the server starts, you can access the web application in your browser at http://localhost:5000.

## Dataset
The dataset used for this project is city_temperature.csv, which contains daily temperature readings from various cities. The data includes:

**Date**: The date of the temperature reading
**City**: The location where the temperature was recorded
**Temperature**: The temperature reading (in Celsius)
The dataset has been cleaned and preprocessed to remove outliers and missing values.

## Results
After comparing all models, Prophet provided the best results. It handled seasonality effectively and delivered the most accurate forecasts for daily temperatures. The model is deployed on a web interface where users can visualize temperature forecasts.

css
