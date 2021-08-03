import flask
import gunicorn
import email_sign_up

from flask import Flask, request, render_template, session, redirect
from flask import send_from_directory

app = flask.Flask(__name__, template_folder='templates', static_folder = 'assets')

@app.route('/', methods=['GET', 'POST'])
def main():

    if flask.request.method == 'GET':

        return flask.render_template('index.html')
    
    if flask.request.method == 'POST':
    	
    	email = flask.request.form['Email']
    	
    	thank_you = email_sign_up.write_to_sheet(email)

        return flask.render_template('index.html', thanks = thank_you)


if __name__ == '__main__':
    app.run()
    
