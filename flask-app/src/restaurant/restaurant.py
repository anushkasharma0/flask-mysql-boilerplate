from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


restaurant = Blueprint('restaurant', __name__)

# Get all restaurants from the DB
@restaurant.route('/restaurant/allRestaurants', methods=['GET'])
def get_restaurants():
    cursor = db.get_db().cursor()
    cursor.execute('select name, rating,\
        price_range from restaurant')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get restaurant detail for restaurant with particular restaurantId
@restaurant.route('/restaurant/<restaurantId>', methods=['GET'])
def get_restaurant_data(restaurantId):
    cursor = db.get_db().cursor()
    cursor.execute('select * from restaurant where restaurantId = {0}'.format(restaurantId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response