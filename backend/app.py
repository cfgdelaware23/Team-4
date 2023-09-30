from flask import Flask, render_template, request, jsonify
#for postgres
import psycopg2
#python file which initializes postgresql database
#import init_db
from model.user import User
from model.inventory import Item
#used for printing out responses to API
import json

app = Flask(__name__)

#home route
@app.route('/')
def home():
    return "Hello!"

#for sign-up page
@app.route("/sign-up",methods=['POST'])
def sign_up():
    user = request.get_json()
    print("Received JSON: %s", json.dumps(user, indent=4))
    #user = []
    try:
        new_user = User.register(user)
        return jsonify({'message': 'Data received successfully', "user": new_user})
    except Exception as e:
        return {"error": str(e)}
        
    #return "Enter your information here"

#login page
@app.route("/login",methods=['GET','POST'])
def login():
    user = []
    User.login(user)
    return "Logged in"

@app.route('/inventory', methods=['GET', 'POST'])
def manage_items():
    if request.method == 'POST':
        items_data = request.get_json()
        try:
            new_items = [Item.add_item(item) for item in items_data]
            return jsonify({'message': f'{len(new_items)} items added successfully', 'items': new_items})
        except Exception as e:
            return {"error": str(e)}
    elif request.method == 'GET':
        try:
            # Assuming you have a method to fetch all items from the database
            items = Item.get_all_items()
            return jsonify({'items': items})
        except Exception as e:
            return {"error": str(e)}

#run the app
if __name__ == '__main__':
    app.run(debug=True,port=55000)