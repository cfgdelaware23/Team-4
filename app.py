from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello!"

@app.route("/sign-up")
def sign_up():
    return "Enter your information here"

if __name__ == '__main__':
    app.run(debug=True)