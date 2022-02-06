import json

import crypto
import database


def login_user(nick_name, pass_word):
    encoded = crypto.encrypt(pass_word)
    logged_in = False
    database.cur.execute(
        "SELECT nickName, password FROM users WHERE nickName =%s", (nick_name,))
    result = database.cur.fetchall()
    for (nickName, password) in result:
        if password == encoded:
            logged_in = True
    return logged_in


def register_user(nick_name, password):
    encoded = crypto.encrypt(password)
    database.cur.execute(
        "SELECT nickName FROM users")
    result = database.cur.fetchall()
    nick_name_exist = False
    for (nickName,) in result:
        if nickName == nick_name:
            nick_name_exist = True
            break
    if not nick_name_exist:
        sql = "INSERT INTO users (nickName, password, score) VALUES (%s, %s, %s)"
        val = (nick_name, encoded, 0)
        database.cur.execute(sql, val)
        database.mydb.commit()
        print(database.cur.rowcount, "record inserted.")
        #database.cur.execute(
        #    "INSERT INTO users (nickName, password, score) VALUES (%s, %s, %s)", (nick_name, encoded, 0)
        #)
        return True
    return False


def get_score(nick_name, pass_word):
    highscore = 0
    encoded = crypto.encrypt(pass_word)
    database.cur.execute(
        "SELECT nickName, password, score FROM users WHERE nickName =%s", (nick_name,))
    result = database.cur.fetchall()
    for (nickName, password, score) in result:
        if password == encoded:
            highscore = score
    return highscore


def update_score(nick_name, pass_word, owned_points):
    new_score = 0
    logged_in = False
    encoded = crypto.encrypt(pass_word)
    database.cur.execute(
        "SELECT nickName, password, score FROM users WHERE nickName =%s", (nick_name,))
    result = database.cur.fetchall()
    for (nickName, password, score) in result:
        if password == encoded:
            logged_in = True
            new_score = int(score) + int(owned_points)
    if logged_in:
        database.cur.execute(
            "UPDATE users SET score =%s WHERE nickName =%s", (new_score, nick_name))
        database.mydb.commit()
        print(database.cur.rowcount, "record updated.")
    return new_score


def get_leader_board(nick_name, pass_word):
    logged_in = False
    encoded = crypto.encrypt(pass_word)
    database.cur.execute(
        "SELECT nickName, password, score FROM users WHERE nickName =%s", (nick_name,))
    result = database.cur.fetchall()
    for (nickName, password, score) in result:
        if password == encoded:
            logged_in = True
    if logged_in:
        database.cur.execute(
            "SELECT nickName, score FROM users ORDER BY score DESC"
        )
        result = database.cur.fetchall()
        users = []
        for user in result:
            x = '{ "nickName":"' + user[0] + '", "score":"' + str(user[1]) + '" }'
            y = json.loads(x)
            # users.append(user)
            users.append(y)
        leader_board_size = 10
        if len(users) < 10:
            leader_board_size = len(users)
        leader_board = []
        count = 0
        while count < leader_board_size:
            print(count)
            leader_board.append(users[count])
            count += 1
        return leader_board
    return False
