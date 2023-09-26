from flask import Flask, render_template #1)need everytime, 2)makes html file readable
from config import Config


app = Flask(__name__) #need everytime
app.config.from_object(Config)


@app.route("/") #single slash is homepage
def index():
    return "Hello from Flask!"

@app.route("/html") #when copying the url in the terminal make sure to add whats in the () to make it go to the correct place
def index_html():
    people = ["Shoha", "Pearl", "Jennifer", "Dimitrius", "Donte", "Brenden"]
    return render_template("index.html", message="Hello from my template", red=True, people=people)

@app.route("/new_html")
def new_html():
    return render_template("base.html")

@app.route("/json")
def json():
    return {"message": "Hello from my updated API!"}

#app.run() #allows it to run --moved to run.py