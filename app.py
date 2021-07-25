import flask
import gunicorn

from flask import Flask, request, render_template, session, redirect
from flask import send_from_directory

app = flask.Flask(__name__, template_folder='templates', static_folder = 'assets')

@app.route('/', methods=['GET', 'POST'])
def main():

    if flask.request.method == 'GET':

        return flask.render_template('index.html')


if __name__ == '__main__':
    app.run()
    
