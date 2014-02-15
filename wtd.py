# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import abort

from htmldiff import htmldiff

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return 'Hello World!'


@app.route('/wtd', methods=['POST'])
def wtd():

    a = request.form.get('a').encode('utf-8').strip()
    b = request.form.get('b').encode('utf-8').strip()

    if a is None or b is None:
        abort(400)


    diff = htmldiff.htmldiff(a, b, accurate_mode=True, addStylesheet=True)
    return diff


if __name__ == '__main__':
    app.debug = True
    app.run()