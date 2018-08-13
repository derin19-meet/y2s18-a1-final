# Database related imports
# Make sure to import your tables!
from model import Base, Company, User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Your database functions are located under here (querying, adding items, etc.)

# Example of adding a student:
def add_company(company_name, company_info, company_link,company_kind):
    print("Added a company!!!")
    company_o = Company(name=company_name, info = company_info, link = company_link, kind = company_kind)
    session.add(company_o)
    session.commit()

def query_by_kind(kind):
	company = session.query(Company).filter_by(
		kind=kind).all()
	return company
def delete_all_companys():
	session.query(Company).delete()
	session.commit()
def add_user(user_username, user_password):
	user1 = User(username = user_username, password = user_password)
	session.add(user1)
	session.commit()

def check_user(username, password):
	users = session.query(User).filter_by(
	username=username).all()
	a=False
	for i in users:
		if (i.password==password):
			a=True
	return a