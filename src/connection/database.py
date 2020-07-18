import mariadb
import sys
import json
from flask import Flask, escape, request, Blueprint


route2 = Blueprint('route2', __name__, template_folder='connection')


@route2.route('/hallo', methods=['GET'])
def get_as_text_route():
    name = 'du da'
    return f'Hello, {escape(name)}!'


class Database():
    route1 = Blueprint('route1', __name__, template_folder='connection')

    def __init__(self):
        try:
            self.conn = mariadb.connect(
                user="quiz",
                password="Brote94",
                host="localhost",
                port=3306,
                database="quiz"
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

        self.cur = self.conn.cursor()
        print("Kein Fehler!")
        print(self.cur)

    def getcur(self):
        return self.cur

    def getquestion(self):
        self.cur.execute(
            "SELECT id, question, rightAnswer, falseAnswer1, falseAnswer2 FROM questions")
        questions = []
        for id, question, rightAnswer, falseAnswer1, falseAnswer2 in self.cur:
            #print(f"{id}: {question}... a) {rightAnswer} b) {falseAnswer1} c) {falseAnswer2}")
            jsonString = {'id': id, 'question': question}
            #jsonString = f'{"id": "{id}", "question": "{question}"}'
            #print(jsonString)
            obj = json.dumps(jsonString)
            #obj = json.loads(jsonString)
            #print(obj)
            questions.append(obj)
        for i in questions:
            print(i)
        return questions


if __name__ == '__main__':
    db = Database()
    print('Methodenaufruf: ' + db.getquestion()[0] + ' ' + db.getquestion()[1])
