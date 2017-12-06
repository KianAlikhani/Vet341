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
	return render_template('vet/index.html')

@app.route('/login', methods=['POST'])
def login():
	o_id = checkOwner(request.form['username'])
	e_id = checkEmployee(request.form['username'])
	if o_id != -1:
		session['o_id'] = o_id
		session['logged_in'] = True
	elif e_id != -1:
		session['e_id'] = e_id
		session['logged_in'] = True
	elif request.form['username'] == 'admin':
		session['admin'] = True
		session['logged_in'] = True
	return redirect('/')

@app.route('/logout')
def logout():
	session['o_id'] = -1
	session['e_id'] = -1
	session['admin'] = False
	session['logged_in'] = False
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

@app.route('/request/getOwnersPets', methods=['GET'])
def request_getOwnersPets():
	o_id = request.args.get('o_id')
	pets = getOwnersPets(o_id)
	jsonPets = jsonify(pets)
	return jsonPets

@app.route('/request/getAppointmentHistory', methods=['GET'])
def request_getAppointmentHistory():
	o_id = request.args.get('o_id')
	pets = getOwnersPets(o_id)
	ret = []
	for pet in pets:
		ret.append(getAppointmentHistory(pet['a_id']))
	return jsonify(ret)

@app.route('/request/getPaymentRecords', methods=['GET'])
def request_getPaymentRecords():
	o_id = request.args.get('o_id')
	paymentRecords = getPaymentRecords(o_id)
	return jsonify(paymentRecords)

@app.route('/request/getPetAppointments', methods=['GET'])
def request_getPetAppointments():
	monthDay = getMonthDay()
	o_id = request.args.get('o_id')
	pets = getOwnersPets(o_id)
	ret = []
	for pet in pets:
		ret.append(getPetAppointments(pet['a_id'], monthDay))
	return jsonify(ret)

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

@app.route('/request/getPerformedProcedures', methods=['GET'])
def request_getPerformedProcedures():
	e_id = request.args.get('e_id')
	performedProcedures = getPerformedProcedures(e_id)
	return jsonify(performedProcedures)

@app.route('/request/getPreviouslyTreatedAnimals', methods=['GET'])
def request_getPreviouslyTreatedAnimals():
	e_id = request.args.get('e_id')
	prevTreatedAnimals = getPreviouslyTreatedAnimals(e_id)
	return jsonify(prevTreatedAnimals)

# Admin Methods

@app.route('/request/getUnpaidBills', methods=['GET'])
def request_getUnpaidBills():
	unpaidBills = getUnpaidBills()
	return jsonify(unpaidBills)

@app.route('/request/getCommonProcedures', methods=['GET'])
def request_getCommonProcedures():
	commonProcedures = getCommonProcedures()
	return jsonify(commonProcedures)

@app.route('/request/getAnimalsWithMostAppointments', methods=['GET'])
def request_getAnimalsWithMostAppointments():
	animalsMostAppointments = getAnimalsWithMostAppointments()
	return jsonify(animalsMostAppointments)

@app.route('/request/getOwnersWithMultAnimals', methods=['GET'])
def request_getOwnersWithMultAnimals():
	ownersWithMultAnimals = getOwnersWithMultAnimals()
	return jsonify(ownersWithMultAnimals)



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