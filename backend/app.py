from flask import Flask, render_template, request, jsonify
#for postgres
#import psycopg2
#from users.donotpush import pass

app = Flask(__name__)

@app.route('/')
def home():

    # conn = psycopg2.connect(
    #     database="postgres", user='postgres', password="password", host='127.0.0.1', port= '5432'
    # )
    # conn.autocommit = True

    # #Creating a cursor object using the cursor() method
    # cursor = conn.cursor()

    # #Preparing query to create a database
    # sql = '''CREATE database mydb''';

    # #  Creating a database
    # cursor.execute(sql)
    # print("Database created successfully........")

    # #Closing the connection
    # conn.close()

    return "Hello!"

@app.route("/sign-up")
def sign_up():
    return "Enter your information here"

if __name__ == '__main__':
    app.run(debug=True)