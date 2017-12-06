from flask import Flask, render_template, request, redirect, session, jsonify
from dbRequests import *
from datetime import date
import json
import os
app = Flask(__name__)

@app.route('/')
def index():
	print(getPaymentRecords(1))
	print(checkLogin("Kian Alikhani"))
	return render_template('index.html')

@app.route('/test')
def testIndex():
	return render_template('testIndex.html')

@app.route('/vet')
def vet():
	return render_template('/templates/vet/index.html')

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

@app.route('/request/getDailyAppointments', methods=['GET', 'POST'])
def request_getDailyAppointments():
	today = date.today()
	#monthday = int(str(today.month).zfill(2) + str(today.day).zfill(2))
	monthday = 1201
	e_id = 1
	dA = getDailyAppointments(e_id, monthday)
	#return '{"e_id": 1, "a_id": 1y}'
	return jsonify(dA)
	
def tupleToDict(row):
    tempEvent = defaultEvent.copy()
    x = 0
    for name in eventTable:
        tempEvent[name] = row[x]
        x += 1
    return tempEvent

if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run(host='0.0.0.0', port=4000)