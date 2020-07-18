from random import randrange

from src.connection import database


def get_question(amount):
    database.cur.execute(
        "SELECT id, question, rightAnswer, falseAnswer1, falseAnswer2 FROM questions")
    questions = []
    for question in database.cur:
        #json_string = {'id': id, 'question': question}
        #obj = json.dumps(json_string)
        questions.append(question)
    random_numbers = []
    i = 0
    while i < amount:
        random = randrange(questions.len())
        # Solange bis random keiner Zahl in random_numbers entspricht neu würfeln
        i += 1
    for i in questions:
        print(i)
    return questions
