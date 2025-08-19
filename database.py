#user
#id firstname secondname age
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker




base = declarative_base()
#This is a representative 
#numbers -> intergers
#decimals ->float
#words ->strings

class User(base):
	__tablename__ = "users"
	id = Column(Integer, primary_key = True)
	firstname = Column(String)
	secondname = Column(String)
	age = Column(Integer)


class Image(base):
	__tablename__ = "Images"
	id = Column(Integer,primary_key = True)
	image_name = Column(String)
	description = Column(String)
	filename = Column(String)



#lets create our database
#sqlite , postgres, cockroachid
connection = create_engine("sqlite:///thedatabase")
base.metadata.create_all(connection)

#a session is alike a key or a house
#helps us use our database
newsession = sessionmaker(connection)
session = newsession()#this session is like a key

#lets create our first user using the key or sesssion
Mwende = User(firstname = "Kndsley", secondname = "Katherina", age=13)
session.add(Mwende)
session.commit()

#---------FETCHING ALL ITEMS IN A DB-------
allusers = session.query(User).all()
for user in allusers:
	print(user.firstname)
	print(user.secondname)
	print(user.age)
	print("------------------")


#---------DELETING AN ITEM FROM A DB-------
session.query(Image).filter_by(id = 4).delete()
session.commit()

#------UPDATING AN ITEM-------
session.query(User).filter_by(secondname = "Katherina").update( {"secondname": "Muli"})
session.commit()

