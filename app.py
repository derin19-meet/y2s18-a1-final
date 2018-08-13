# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request
from flask import session as login_session

# Add functions you need from databases.py to the next line!
from databases import *

# Starting the flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = "Your_secret_string"

# App routing code here
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/addcompany', methods=['GET', 'POST'])
def add_company_route():
	if request.method == 'GET':
		return render_template('addcompany.html')
	else:
		add_company(request.form['company_name'],request.form["company_info"],request.form["company_link"],request.form["company_kind"])
		return redirect(url_for('home'))

@app.route('/adduser', methods=['GET', 'POST'])
def add_user_route():
	if request.method == 'GET':
		return render_template('newprofile.html')
	else:
		add_user(request.form['username'],request.form["password"])
		return redirect(url_for('choose'))

@app.route('/choice')
def choose():
    return render_template("user.html")

@app.route('/login', methods=['GET', 'POST'])
def user_login():
	if request.method == 'POST':
		if (check_user(request.form['username'],request.form["password"])):
			user=query_by_username(request.form['username'])
			login_session['id']=user.id
			login_session['username']=user.username
			return redirect(url_for('choose'))
		else:
			return render_template("login.html")
	else:
		return render_template("login.html")

@app.route('/logout')
def user_logout():
		del login_session['id']
		del login_session['username']
		return redirect(url_for('home'))


@app.route('/about')
def aboutus():
    return render_template("about.html")


@app.route('/donate/<comp_kind>')
def donate_something(comp_kind):
    things = query_by_kind(comp_kind)
    return render_template('donations.html', things=things, comp_kind=comp_kind)

# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
