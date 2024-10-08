from flask import Flask, request, jsonify, render_template
from prophet import Prophet
import pandas as pd

app = Flask(__name__, static_folder='static')

# Load your entire dataset from the database
# and preprocess the data to get it ready for modeling
data = pd.read_csv('city_temperature.csv')
data = data.drop(['State'], axis=1)
data = data.drop_duplicates()
data = data[data['Year'] > 1994]
data = data[data['Year'] < 2020]
data = data[data['Day'] > 0]

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict_temperature', methods=['GET'])
def predict_temperature():
    country = request.args.get('country')
    city = request.args.get('city')
    date_str = request.args.get('date')

    try:
        date = pd.to_datetime(date_str)
    except ValueError:
        return jsonify({"error": "Invalid date format. Please use 'YYYY-MM-DD'."}), 400

    # Filter the data for the user-specified country and city
    country_data = data[(data["Country"] == country) & (data["City"] == city)]
    country_data = country_data[country_data["AvgTemperature"] != -99]
    country_data["TempInC"] = country_data["AvgTemperature"].apply(lambda x: (x - 32) / 1.8)
    country_data["datetime"] = country_data.apply(lambda x: pd.to_datetime(f"{x['Year']}-{x['Month']}-{x['Day']}"), axis=1)
    country_data.index = country_data["datetime"].values
    n_df = country_data[['datetime', 'TempInC']]
    n_df.rename(columns={'datetime': 'ds', 'TempInC': 'y'}, inplace=True)

    if n_df.empty:
        return jsonify({"error": "Data not available for the given country and city."}), 404

    try:
        model = Prophet()
        model.fit(n_df)

        future_df = model.make_future_dataframe(periods=365 * 10)  # Forecast for the next 10 years
        forecast = model.predict(future_df)
        prediction = forecast.loc[forecast['ds'] == date, 'yhat'].values[0]
        return render_template('result.html', temperature=prediction)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
