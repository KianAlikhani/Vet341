from flask import Flask, render_template, request, redirect, session, jsonify
from dbRequests import *
from datetime import datetime, date, timedelta
import json
import os
app = Flask(__name__)

@app.route('/')
def index():
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

# Owner Methods
@app.route('/request/getAvailableVets', methods=['GET'])
def request_getAvailableVets():
	monthDay, hourMin = parseDateTime(datetime.now())
	return jsonify(getAvailableVets(monthDay, hourMin))

@app.route('/request/getPaymentRecords', methods=['GET'])
def request_getPaymentRecords():
	o_id = request.args.get('o_id')
	paymentRecords = getPaymentRecords(o_id)
	return jsonify(paymentRecords)

# Vet Methods
@app.route('/request/getDailyAppointments', methods=['GET'])
def request_getDailyAppointments():
	today = date.today()
	#monthday = int(str(today.month).zfill(2) + str(today.day).zfill(2))
	monthday = 1201
	e_id = request.args.get('e_id')
	dA = getDailyAppointments(e_id, monthday)
	#return '{"e_id": 1, "a_id": 1y}'
	return jsonify(dA)

def parseDateTime(now):
	return (int(str(now.month).zfill(2) + str(now.day).zfill(2)), parseHourMinute(now, timedelta(minutes=15)))

def parseHourMinute(now, delta):
	return int(str(now.hour % 12) + str((now + (datetime.min - now) % delta).minute).zfill(2))

def getMonthDay():
	today = date.today()
	return int(str(today.month).zfill(2) + str(today.day).zfill(2))

if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run(host='0.0.0.0', port=4000)