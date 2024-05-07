from flask import Flask, jsonify

from scraping import *

app = Flask(__name__)

@app.route('/api/patelbros/<search_query>', methods=['GET'])
def get_prices_patelbros(search_query):
    prices = get_price_patelbros(search_query, 'Chicago')  # Using the function from above
    return jsonify(prices)


@app.route('/api/petsmart/<search_query>', methods=['GET'])
def get_prices_petsmart(search_query):
    prices = get_price_petsmart(search_query)  # Using the function from above
    return jsonify(prices)


@app.route('/api/target/<search_query>', methods=['GET'])
def get_prices_target(search_query):
    prices = get_price_target(search_query)  # Using the function from above
    return jsonify(prices)


@app.route('/api/meijer/<search_query>', methods=['GET'])
def get_prices_meijer(search_query):
    prices = get_price_meijer(search_query)  # Using the function from above
    return jsonify(prices)


@app.route('/api/costco/<search_query>', methods=['GET'])
def get_prices_costco(search_query):
    prices = get_price_costco(search_query)  # Using the function from above
    return jsonify(prices)


@app.route('/api/walmart/<search_query>', methods=['GET'])
def get_prices_walmart(search_query):
    prices = get_price_costco(search_query)  # Using the function from above
    return jsonify(prices)

if __name__ == '__main__':
    app.run(debug=True)
