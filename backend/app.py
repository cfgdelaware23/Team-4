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
@app.route("/sign-up",methods=['GET','POST'])
def sign_up():
    user = []
    try:
        print(User.register(user))
        return {"message": "success"}
    except:
        pass
    return "Enter your information here"

#login page
@app.route("/login",methods=['GET','POST'])
def login():
    user = []
    User.login(user)
    return "Logged in"



#run the app
if __name__ == '__main__':
    app.run(debug=True,port=55000)
