from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    if name:
        newName = name[::-1]
        return jsonify({'name': newName})
    return jsonify({'error': 'Missing data!'})


















