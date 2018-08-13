# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
from databases import add_company, query_by_kind

# Starting the flask app
app = Flask(__name__)

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

@app.route('/donate/<comp_kind>')
def donate_something(comp_kind):
    things = query_by_kind(comp_kind)
    return render_template('donations.html', things=things)

# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
