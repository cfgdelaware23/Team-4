from flask import Flask, render_template, request, jsonify
#for postgres
<<<<<<< HEAD
import psycopg2
#python file which initializes postgresql database
import init_db
=======
#import psycopg2
#from users.donotpush import pass
# from model.user import User
>>>>>>> 98075f946b096d8bde97864a3c0ea94c6f00ca18

app = Flask(__name__)

#home route
@app.route('/')
def home():
    return "Hello!"

#for sign-up page
@app.route("/sign-up")
def sign_up():
    return "Enter your information here"

#run the app
if __name__ == '__main__':
    app.run(debug=True)
    init_db.set_up()

