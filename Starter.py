from flask import Flask
from flask import render_template
from flask import request
from database import Image
from database import session
from flask import redirect
#print(__name__)
app = Flask(__name__)

@app.route("/")
def homepage():
	allimages = session.query(Image).all()
	return render_template("Pinspire.html",allimages = allimages)

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/create")
def create():
	return render_template("pinspirecreate.html")


#this will be responsible for saving images
@app.route("/save", methods =["POST"])
def save():
	print(request.form)
	Imagename = request.form["imagename"]
	description = request.form["description"]
	picture = request.files["image"]
	newImage = Image(image_name = Imagename, description = description,filename = picture.filename)
	picture.save(dst = rf"C:\Users\PC\Desktop\Flask\static\All pictures\{picture.filename}")
	session.add(newImage)
	session.commit()

	return redirect("/") #Does not return anything important


app.run()

