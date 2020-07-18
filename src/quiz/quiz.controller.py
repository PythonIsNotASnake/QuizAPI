from flask import Blueprint, escape

route2 = Blueprint('route2', __name__, template_folder='connection')


@route2.route('/hallo', methods=['GET'])
def get_as_text_route():
    name = 'du da'
    return f'Hello, {escape(name)}!'