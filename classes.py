score = "97"
name= "Mwende"
#person (firstname, lastname,)
#(age, race, religion)
#VEHICLE
#(brand, color, model, wheels, price)


class Person:
	firstname = ""
	secondname = ""
	age = ""
	race = ""

#Abu
Abu = Person()
Abu.firstname = "Abu"
Abu.secondname = "Doe"
Abu.age = "20"
Abu.race = "Black"
print(Abu.firstname)
print(Abu.secondname)
print(Abu.age)
print(Abu.race)

#Maltea
Maltea = Person()
Maltea.firstname = "Maltea"
Maltea.secondname = "Muli"
Maltea.age = 21
Maltea.race = "Black"

print(Maltea.firstname)
print(Maltea.secondname)
print(Maltea.age)
print(Maltea.race)

#Mercedes
class vehicle:

	brand = "Mercedes_benz"
	color = "black"
	model = "GLE COUPE 2024"

Mercedes_benz = vehicle()

print(Mercedes_benz.brand)
print(Mercedes_benz.color)
print(Mercedes_benz.model)

import flask_sqlalchemy
