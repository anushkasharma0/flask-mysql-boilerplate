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

# Get price range for restaurant with particular restaurantId
@restaurant.route('/restaurant/pricerange/<restaurantId>', methods=['GET'])
def get_pricerange(restaurantId):
    cursor = db.get_db().cursor()
    cursor.execute('select price_range from restaurant where restaurantId = {0}'.format(restaurantId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get rating for restaurant with particular restaurantId
@restaurant.route('/restaurant/rating/<restaurantId>', methods=['GET'])
def get_rating(restaurantId):
    cursor = db.get_db().cursor()
    cursor.execute('select rating from restaurant where restaurantId = {0}'.format(restaurantId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get location for restaurant with particular restaurantId
@restaurant.route('/restaurant/location/<restaurantId>', methods=['GET'])
def get_location(restaurantId):
    cursor = db.get_db().cursor()
    cursor.execute('select street_address, city, state, zip_code from location where restaurantId = {0}'.format(restaurantId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get recommendation for restaurant with particular restaurantId
@restaurant.route('/restaurant/recommendation/<restaurantId>', methods=['GET'])
def get_recommendation(restaurantId):
    cursor = db.get_db().cursor()
    cursor.execute('select recommendations from experience where restaurantId = {0}'.format(restaurantId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get criticisms for restaurant with particular restaurantId
@restaurant.route('/restaurant/criticisms/<restaurantId>', methods=['GET'])
def get_criticisms(restaurantId):
    cursor = db.get_db().cursor()
    cursor.execute('select criticisms from experience where restaurantId = {0}'.format(restaurantId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get service rating for restaurant with particular restaurantId
@restaurant.route('/restaurant/servicerating/<restaurantId>', methods=['GET'])
def get_service_rating(restaurantId):
    cursor = db.get_db().cursor()
    cursor.execute('select rating from service where restaurantId = {0}'.format(restaurantId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get menu rating for restaurant with particular restaurantId
@restaurant.route('/restaurant/menurating/<restaurantId>', methods=['GET'])
def get_menu_rating(restaurantId):
    cursor = db.get_db().cursor()
    cursor.execute('select rating from menu where restaurantId = {0}'.format(restaurantId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Post information about new restaurant
@restaurant.route('/restaurant', methods=['POST'])
def add_new_restaurant():
     
     # collecting data from the request object
     the_data = request.json
     current_app.logger.info(the_data)


     # extracting the variable
     name = the_data['name']
     rating = the_data['rating']
     price = the_data ['price_range']
     
     # constructing the query
     query = 'insert into restaurant(name, rating, price_range) values ("'
     query += name + '", "'
     query += str(rating) + '", "'
     query += price + '")'
     current_app.logger.info(query) 
     
     # executing and committing the insert statement
     cursor = db.get_db().cursor()
     cursor.execute(query)
     db.get_db().commit()

     return 'Success!'

# Put - Update rating of a restaurant
@restaurant.route('/restaurant/updaterestaurant/<RestaurantId>', methods=['PUT'])
def update_review(restaurant_id, review_id):
    # Check if the restaurant exists
    restaurant = next((r for r in restaurant_reviews if r['restaurant_id'] == restaurant_id), None)
    if restaurant is None:
        return jsonify({'error': 'Restaurant not found'}), 404

    # Check if the review exists
    review = next((r for r in restaurant_reviews if r['id'] == review_id), None)
    if review is None:
        return jsonify({'error': 'Review not found'}), 404

    # Get updated data from the request
    updated_data = request.get_json()
    if not updated_data:
        return jsonify({'error': 'No data provided'}), 400

    # Update review data
    review['rating'] = updated_data.get('rating', review['rating'])
    review['comment'] = updated_data.get('comment', review['comment'])

    # Return updated review data
    return jsonify({'message': 'Review updated successfully', 'review': review}), 200

if __name__ == '__main__':
    app.run(debug=True)


# Delete restaurant given a RestaurantId
@restaurant.route('/restaurant/deleterestaurant/<RestaurantId>', methods=['DELETE'])
def delete_user(RestaurantId):
    cursor = db.get_db().cursor()
    cursor.execute('select RestaurantId from restaurant where RestaurantId= {0}'.format(RestaurantId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return 'Restaurant deleted'
