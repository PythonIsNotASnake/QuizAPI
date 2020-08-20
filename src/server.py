from flask import Flask, escape, request, render_template

from auth import auth_controller
from quiz import quiz_controller

app = Flask(__name__, template_folder='src')
app.register_blueprint(quiz_controller.quizController, url_prefix="/quiz")
app.register_blueprint(auth_controller.authController, url_prefix="/auth")
# database


@app.route('/', methods=['GET'])
def hello():
    name = request.args.get("name", "World")
    return name


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1337, debug=True)
    #app.run(port=1337, debug=True, ssl_context='adhoc')