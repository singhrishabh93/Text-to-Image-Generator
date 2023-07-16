# AI Text to Image generator using Dall-e
from flask import Flask
from config import key
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'


app.run(host='0.0.0.0', port=81)
