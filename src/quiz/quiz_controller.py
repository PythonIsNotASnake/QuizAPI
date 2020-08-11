from flask import Blueprint, escape, jsonify
from src.quiz import quiz_service

quizController = Blueprint('quizController', __name__, template_folder='src')


@quizController.route('/<amount>', methods=['GET'])
def get_questions(amount):
    # return f'Hello, {escape(obj[0])}!'
    questions = quiz_service.get_question(amount)
    return jsonify(questions=questions)
