from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


socialuser = Blueprint('socialuser', __name__)

# Get all usernames from the DB
@socialuser.route('/socialuser/allUsers', methods=['GET'])
def get_usernames():
    cursor = db.get_db().cursor()
    cursor.execute('select username from user')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get all information for user with particular UserId
@socialuser.route('/socialuser/<UserId>', methods=['GET'])
def get_user_info(UserId):
    cursor = db.get_db().cursor()
    cursor.execute('select * from user where UserId = {0}'.format(UserId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response 

# Get all posts for user with particular UserId
@socialuser.route('/socialuser/getposts/<UserId>', methods=['GET'])
def get_post_info(UserId):
    cursor = db.get_db().cursor()
    cursor.execute('select * from post where UserId = {0}'.format(UserId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response 

# Get blocking status given a FollowerId
@socialuser.route('/socialuser/blocked/<FollowerId>', methods=['GET'])
def get_blocked(FollowerId):
    cursor = db.get_db().cursor()
    cursor.execute('select blocking_status from friend where FollowerId= {0}'.format(FollowerId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response 

# Get photos given a PostId
@socialuser.route('/socialuser/photos/<PostId>', methods=['GET'])
def get_photos(PostId):
    cursor = db.get_db().cursor()
    cursor.execute('select photo from pictures where PostId= {0}'.format(PostId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response 

# Get comments given a PostId
@socialuser.route('/socialuser/comments/<PostId>', methods=['GET'])
def get_comments(PostId):
    cursor = db.get_db().cursor()
    cursor.execute('select text from comment where PostId= {0}'.format(PostId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response 

# Get comments given a PostId
@socialuser.route('/socialuser/reactions/<PostId>', methods=['GET'])
def get_reactions(PostId):
    cursor = db.get_db().cursor()
    cursor.execute('select type from reaction where PostId= {0}'.format(PostId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Post a post
# Put
# Delete


