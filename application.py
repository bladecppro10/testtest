import click
from flask import Flask
from flask_cli import  FlaskCLI
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Yo Im alive'