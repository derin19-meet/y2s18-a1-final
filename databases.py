# Database related imports
# Make sure to import your tables!
from model import Base, Company

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
