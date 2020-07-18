from src.auth import crypto
from src.connection import database


def login_user(nick_name, password):
    encoded = crypto.encrypt(password)
    logged_in = False
    database.cur.execute(
        "SELECT nickName, password FROM users WHERE nickName =?", (nick_name,))
    for user in database.cur:
        if user[1] == encoded:
            logged_in = True
    return logged_in


def register_user(nick_name, password):
    encoded = crypto.encrypt(password)
    database.cur.execute(
        "INSERT INTO users (nickName, password, score) VALUES (?, ?, ?)", (nick_name, encoded, 0)
    )


def get_score(nick_name, password):
    highscore = 0
    encoded = crypto.encrypt(password)
    database.cur.execute(
        "SELECT nickName, password, score FROM users WHERE nickName =?", (nick_name,))
    for user in database.cur:
        if user[1] == encoded:
            highscore = user[2]
    return highscore


def update_score(nick_name, password, owned_points):
    new_score = 0
    logged_in = False
    encoded = crypto.encrypt(password)
    database.cur.execute(
        "SELECT nickName, password, score FROM users WHERE nickName =?", (nick_name,))
    for user in database.cur:
        if user[1] == encoded:
            logged_in = True
            new_score = user[2] + owned_points
    if logged_in:
        database.cur.execute(
            "UPDATE users SET score =? WHERE nickName =?", (new_score, nick_name))
    return new_score
