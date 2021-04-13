from flask import Flask, render_template, request, jsonify

from app.bot import app_grandpy

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/question', methods=['POST'])
def question():
    if request.method == 'POST':
        question = request.form['submitText']
        answer = app_grandpy(question)
        return jsonify(answer)
