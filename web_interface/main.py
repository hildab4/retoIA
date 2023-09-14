# Import necessary libraries
from flask import Flask, render_template, request
import joblib
import pandas as pd


app = Flask(__name__, template_folder='templates')

# Load the pre-trained model
model = joblib.load('web_interface\modelo_reto.sav')

# Read the train info, used to rename columns for predicted DataFrame
stores_sales = pd.read_csv('web_interface/datasets/train.csv', usecols=['store_nbr', 'family', 'date', 'sales'], dtype={'store_nbr': 'category', 'family': 'category', 'sales': 'float32'}, parse_dates=['date'], infer_datetime_format=True)
# Convert date column to Period Index object, daily
stores_sales['date'] = stores_sales.date.dt.to_period('D')
# Set index, later used for predicted DataFrame
stores_sales = stores_sales.set_index(['store_nbr', 'family', 'date']).sort_index()
# Unstack values by store_nbr and family, later used for predicted DataFrame
y = stores_sales.unstack(['store_nbr', 'family']).loc['2017':'2017-08-15']

# Main route
@app.route('/')
def index():
    return render_template('index.html')

# Predict route
@app.route('/predict', methods=['POST', 'GET'])
def predict():
    # Get user inputs
    store_number = request.form['Store_Number']
    product_family = request.form['Product_Family']
    date = request.form['Date']

    # Read DataFrame with fourier transforms and dummies
    x = pd.read_csv('web_interface/datasets/x_in.csv')
    x = x.set_index('date')

    # Filter by the date input
    x = x.loc[(x.index == date)]

    # Make prediction using the pre trained model
    final = pd.DataFrame(model.predict(x), index = x.index, columns = y.columns)
    prediction = final.loc(axis=1)['sales', store_number, product_family][0]

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)