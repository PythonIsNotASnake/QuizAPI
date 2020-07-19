from flask import Blueprint, escape, request, jsonify

from src.auth import auth_service

authController = Blueprint('authController', __name__, template_folder='src')


@authController.route('/register', methods=['POST'])
def post_account():
    data = request.get_json()
    nick_name = data['nickName']
    password = data['password']
    registered = auth_service.register_user(nick_name, password)
    return jsonify(registered)


@authController.route('/login', methods=['PUT'])
def post_login():
    data = request.get_json()
    nick_name = data['nickName']
    password = data['password']
    logged_in = auth_service.login_user(nick_name, password)
    return jsonify(logged_in)


@authController.route('/score', methods=['PUT'])
def get_score():
    data = request.get_json()
    nick_name = data['nickName']
    password = data['password']
    highscore = auth_service.get_score(nick_name, password)
    return jsonify(highscore)


@authController.route('/score', methods=['PUT'])
def update_score():
    data = request.get_json()
    nick_name = data['nickName']
    password = data['password']
    points = data['points']
    highscore = auth_service.update_score(nick_name, password, points)
    return jsonify(highscore)


@authController.route('/leaderboard', methods=['PUT'])
def get_leader_board():
    data = request.get_json()
    nick_name = data['nickName']
    password = data['password']
    leader_board = auth_service.get_leader_board(nick_name, password)
    return jsonify(leader_board)
