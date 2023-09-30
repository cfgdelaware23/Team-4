from flask import Flask, render_template, request, jsonify
#for postgres
import psycopg2
#python file which initializes postgresql database
#import init_db
from model.user import User
from model.inventory import Item
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
@app.route("/sign-up",methods=['GET','POST'])
def sign_up():
    try:
         #user = request.get_json()
        user = json.loads(request.form['user'])
        print("Received JSON: %s", json.dumps(user, indent=4))
        #user = []
    
        #incorporating photo upload and handing it off to another function
        if 'image' in request.files:
            image_file = request.files['image']
            image_filename = save_uploaded_image(image_file)

        new_user = User.register(user)
        print("image filename",image_filename)
        return jsonify({'message': 'Data received successfully', "user": new_user})

    except Exception as e:
        return jsonify({"error": str(e)})
        
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
        
def save_uploaded_image(image_file):
    if image_file.filename != '':
        # Generate a unique filename or use a specific naming convention
        image_filename = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
        image_file.save(image_filename)
        process_image(image_filename)
        return image_filename
    return None

# @app.route("/process-image", methods=['GET'])
# def process_image():
#     import image_to_text
#     while not os.path.exists("recognized.txt"):
#         time.sleep(1)  # Wait for 1 second before checking again
#         #print("hi")

#     try:
#         with open("recognized.txt", "r") as f:
#             recognized_text = f.read()
#         return jsonify({"recognized_text": recognized_text})

#     except Exception as e:
#         return jsonify({"error": str(e)})

def process_image(image_filename):
    import image_to_text
    while not os.path.exists("recognized.txt"):
        time.sleep(1)  # Wait for 1 second before checking again
        #print("hi")
    
    print("success")

    # Once the file exists, open and read it
    with open("recognized.txt", "r") as f:
        print(f.read())
    #f = open("recognized.txt", "r")
    #print(f.read())
    #f.close()


#run the app
if __name__ == '__main__':
    app.run(debug=True,port=55000)