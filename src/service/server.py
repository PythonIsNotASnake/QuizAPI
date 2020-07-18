from flask import Flask, escape, request

from src.connection import database
from src.connection.database import Database

app = Flask(__name__, template_folder='connection')
db = Database()
app.register_blueprint(db.route1, url_prefix="/route1")
app.register_blueprint(database.route2, url_prefix="/route2")


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


if __name__ == '__main__':
    app.run(port=1337, debug=True)