import flask
import gunicorn
import gspread
import os
import email_sign_up

from flask import Flask, request, render_template, session, redirect
from flask import send_from_directory

app = flask.Flask(__name__, template_folder='templates', static_folder = 'assets')

@app.route('/', methods=['GET', 'POST'])
def main():

    if flask.request.method == 'GET':

        return flask.render_template('index.html')
    
    if flask.request.method == 'POST':
    	
    	name = flask.request.form['name']
    	email = flask.request.form['email']
    	telephone = flask.request.form['telephone']
    	quantity = flask.request.form['quantity']
    	arrival = flask.request.form['arrival']
    	departure = flask.request.form['departure']
    	message = flask.request.form['message']
    	
    	thank_you = email_sign_up.write_to_sheet(name, email, telephone, quantity, arrival, departure, message)
    	
    	return flask.render_template('index.html', thanks = thank_you)

@app.errorhandler(500)
def pageNotFound(error):
    return flask.render_template('500.html')

if __name__ == '__main__':
    app.run()
    
