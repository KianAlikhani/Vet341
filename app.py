from flask import Flask, render_template, request, redirect, session
from dbRequests import *
import json
import os
app = Flask(__name__)

@app.route('/')
def index():
	print(getPaymentRecords(1))
	print(checkLogin("Kian Alikhani"))
	print(checkLogin("Kevin G"))
	return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
	if request.form['password'] == 'pass' and request.form['username'] == 'user':
		session['logged_in'] = True
		session['admin'] = False
	elif request.form['password'] == 'pass' and request.form['username'] == 'admin':
		session['logged_in'] = True
		session['admin'] = True
	return redirect('/')

@app.route('/logout')
def logout():
	session['logged_in'] = False
	session['admin'] = False
	return redirect('/')

@app.route('/request/getUserInfo', methods=['GET'])
def request_getUserInfo():
	if request.method == 'GET':
		sampleJsonData = '[{"o_id": 1, "o_name": "John Doe", "o_address": "123 Street", "phone_number": 1234567890}, {"o_id": 2, "o_name": "Jane Doe", "o_address": "321 Street", "phone_number": 0987654321}]'
		return sampleJsonData

@app.route('/request/testLogin', methods=['POST'])
def request_testLogin():
	if request.method == 'POST':
		print("POSTED SUCCESSFULLY!")
	return redirect('/')

if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run(host='0.0.0.0', port=4000)