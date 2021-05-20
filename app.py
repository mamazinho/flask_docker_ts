import sys, os
sys.path.append(os.getcwd())

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return 'deu tudo certo'

# app.run(debug=True, port=5000)
