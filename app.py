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
	if (login_session.get('username')!=None):
		user1=query_by_username(login_session['username'])
		return render_template('home.html', user1 = user1)
	else:
		return render_template('home_witout_user.html')


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
		if (request.form["password"]==request.form["repassword"]):
			add_user(request.form['username'],request.form["password"] , "")
			return redirect(url_for('home'))
		else:
			return render_template('newprofile.html')

@app.route('/choice')
def choose():
	if (login_session.get('username')!=None):
		user1=query_by_username(login_session['username'])
		return render_template("user.html", user1=user1)
	else:
		return render_template("login.html")

@app.route('/donate_to_comp/<comp_id>')
def add_to_profile(comp_id):
	if (login_session.get('username')!=None):
		user1=query_by_username(login_session['username'])
		add_comp_to_user(user1, comp_id)
		comp1 = query_comp_id(comp_id)
	return redirect(url_for("donate_something",comp_kind=comp1.kind))




@app.route('/profile')
def your_profile():
	if (login_session.get('username')!=None):
		user1=query_by_username(login_session['username'])
		companys = (user1.donate).split(" ")
		stringofnames = " "
		for a in companys:
			b = query_comp_id(int(a)) 
			stringofnames+= " " + b.name
		return render_template("profile.html", user1=user1, stringofnames = stringofnames)
	else:	
		return redirect(url_for('home'))

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
	if (login_session.get('username')!=None):
		del login_session['id']
		del login_session['username']
		return redirect(url_for('home'))
	else:
		return redirect(url_for('home'))


@app.route('/about')
def aboutus():
	return render_template("about.html")




@app.route('/donate/<comp_kind>')
def donate_something(comp_kind):
	user1=query_by_username(login_session['username'])
	things = query_by_kind(comp_kind)
	return render_template('donations.html', things=things, comp_kind=comp_kind, user1=user1)
# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
