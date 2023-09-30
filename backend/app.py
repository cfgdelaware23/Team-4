from flask import Flask, render_template, request, jsonify
#for postgres
import psycopg2
#python file which initializes postgresql database
import init_db
from model.user import User

app = Flask(__name__)

#home route
@app.route('/')
def home():
    return "Hello!"

#for sign-up page
@app.route("/sign-up",)
def sign_up():
    User.register()
    return "Enter your information here"

#login page
@app.route("/login")
def login():
    User.login("hey")
    return "Logged in"



#run the app
if __name__ == '__main__':
    app.run(debug=True,port=55000)
