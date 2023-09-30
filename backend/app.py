from flask import Flask, render_template, request, jsonify
#for postgres
import psycopg2
#python file which initializes postgresql database
#import init_db
from model.user import User
#used for printing out responses to API
import json
#needed for folder creation/file portion
import os 

app = Flask(__name__)
#logic for photo uploads (optional)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#home route
@app.route('/')
def home():
    return "Hello!"

#for sign-up page
@app.route("/sign-up",methods=['POST'])
def sign_up():
    #user = request.get_json()
    user = json.loads(request.form['user'])
    print("Received JSON: %s", json.dumps(user, indent=4))
    #user = []
    
    #incorporating photo upload and handing it off to another function
    if 'image' in request.files:
        image_file = request.files['image']
        image_filename = save_uploaded_image(image_file)

    try:
        new_user = User.register(user)
        print("image filename",image_filename)
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

def save_uploaded_image(image_file):
    if image_file.filename != '':
        # Generate a unique filename or use a specific naming convention
        image_filename = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
        image_file.save(image_filename)
        return image_filename
    return None


#run the app
if __name__ == '__main__':
    app.run(debug=True,port=55000)
