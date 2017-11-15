from flask import Flask, render_template, request, redirect, session
import os
app = Flask(__name__)

@app.route('/')
def index():
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


if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run(host='0.0.0.0', port=4000)