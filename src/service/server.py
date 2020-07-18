from flask import Flask, escape, request

from src.auth import auth_controller
from src.quiz import quiz_controller

app = Flask(__name__, template_folder='src')
app.register_blueprint(quiz_controller.quizController, url_prefix="/quiz")
app.register_blueprint(auth_controller.authController, url_prefix="/auth")
# database


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


if __name__ == '__main__':
    app.run(port=1337, debug=True)