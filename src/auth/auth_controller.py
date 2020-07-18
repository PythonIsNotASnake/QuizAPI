from flask import Blueprint, escape, request, jsonify

from src.auth import auth_service

authController = Blueprint('authController', __name__, template_folder='src')


@authController.route('/register', methods=['POST'])
def post_account():
    data = request.get_json()
    nick_name = data['nickName']
    password = data['password']
    auth_service.register_user(nick_name, password)


@authController.route('/login', methods=['POST'])
def post_login():
    data = request.get_json()
    nick_name = data['nickName']
    password = data['password']
    logged_in = auth_service.login_user(nick_name, password)
    return jsonify(logged_in)


@authController.route('/score', methods=['GET'])
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
