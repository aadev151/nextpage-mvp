
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, render_template, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    with open('/home/nextpage/mysite/yesno.json', 'w') as file:
        file.write('{"refresh": 1}')
        return render_template('success.html')


@app.route('/get')
def get_yesno():
    with open('/home/nextpage/mysite/yesno.json') as file:
        return jsonify(file.read())
