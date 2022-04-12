from flask import Flask

app = Flask(__name__)

from application import routes

app.config['SECRET_KEY'] = 'e0b3b359461fab01e70f38bbee9045e9'
