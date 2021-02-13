

import os

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def question():
    return render_template('index.html')
















