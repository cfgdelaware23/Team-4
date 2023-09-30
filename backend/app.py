from flask import Flask, render_template, request, jsonify
#for postgres
import psycopg2
#python file which initializes postgresql database
#import init_db
from model.user import User
#used for printing out responses to API
import json

app = Flask(__name__)

#home route
@app.route('/')
def home():
    return "Hello!"

#for sign-up page
@app.route("/sign-up",methods=['GET','POST'])
def sign_up():
    user = request.get_json()
    print("Received JSON: %s", json.dumps(user, indent=4))
    #user = []
    User.register(user)
    return jsonify({'message': 'Data received successfully'})
    #return "Enter your information here"

#login page
@app.route("/login",methods=['GET','POST'])
def login():
    user = []
    User.login(user)
    return "Logged in"



#run the app
if __name__ == '__main__':
    app.run(debug=True,port=55000)
