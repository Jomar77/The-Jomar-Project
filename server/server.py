from flask import Flask, request, jsonify
import util


app = Flask(__name__)

@app.route('/predict')

def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home', methods=['POST'])

def predict_home_price():
    area = float(request.form['area'])
    location = request.form['location']
    room = int(request.form['rooms'])
    bath = int(request.form['bathroom'])
    age = int(request.form['age'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, area, room, bath,age)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response



if(__name__ == '__main__'):
    print("Starting Python Flask Server For House Price Prediction...")
    app.run(debug=True)
