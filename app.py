from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "Honeycred Injector Running"

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    with open("log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - Attempt: {username} / {password}\n")

    return "Access Logged"

if __name__ == "__main__":
    app.run(debug=True)
