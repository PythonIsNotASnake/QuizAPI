from flask import Blueprint, escape, jsonify, request
import quiz_service

quizController = Blueprint('quizController', __name__, template_folder='src')


@quizController.route('/<amount>', methods=['GET'])
def get_questions(amount):
    # return f'Hello, {escape(obj[0])}!'
    questions = quiz_service.get_question(amount)
    return jsonify(questions=questions)


@quizController.route('/create', methods=['POST'])
def post_question():
    data = request.get_json()
    question = data['question']
    right_answer = data['rightAnswer']
    false_answer1 = data['falseAnswer1']
    false_answer2 = data['falseAnswer2']
    question = quiz_service.create_question(question, right_answer, false_answer1, false_answer2)
    return jsonify(question=question)
