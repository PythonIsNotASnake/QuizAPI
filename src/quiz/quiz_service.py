from random import randrange

from src.connection import database


def get_question(amount):
    database.cur.execute(
        "SELECT id, question, rightAnswer, falseAnswer1, falseAnswer2 FROM questions")
    questions = []
    for question in database.cur:
        questions.append(question)
    i = 0
    randoms = []
    if int(amount) < len(questions):
        while i < int(amount):
            reach_end = False
            while not reach_end:
                zufall = randrange(len(questions))
                j = 0
                if len(randoms) == 0:
                    randoms.append(zufall)
                    i += 1
                    break
                while j < len(randoms):
                    if randoms[j] == zufall:
                        reach_end = True
                        break
                    if j == len(randoms) - 1:
                        randoms.append(zufall)
                        i += 1
                        reach_end = True
                        break
                    j += 1
    random_questions = []
    q = 0
    while q < len(randoms):
        random_questions.append(questions[randoms[q]])
        q += 1
    return random_questions
