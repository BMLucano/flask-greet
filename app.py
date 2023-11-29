from flask import Flask

app = Flask(__name__)

@app.get("/welcome")
def welcome():
    return "welcome"

@app.get("/welcome/back")
def welcome_back():
    return "welcome back"

@app.get("/welcome/home")
def welcome_home():
    return "welcome home"