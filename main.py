# Name: Isaac Francisco Marte
# Class: SDEV 300

# import modules used within program for flask, datetime, and random
from flask import Flask, render_template, request
from datetime import datetime
from random import randint
from passlib.hash import sha256_crypt
# import numpy as np

app = Flask(__name__)  # Creates flash app instance

users = []


@app.route('/long', methods=['GET', 'POST'])
def long():
    first = ''
    message = ''
    return render_template('long.html', first=first, message=message)


@app.route('/lucky')   # Decorator for URL route to webpage
def number_generator():
    
    """number_generator function uses the @app.route module with the created route name for the webpage being lucky 
    which creates a number variable with a value of a random number and returns the template and number"""
    
    number = randint(1, 100)  # number variable is used to store a random value between 1 - 10

    return render_template('lucky.html', number=number)  # returns the webpage and random number generated


@app.route('/', methods=['GET', 'POST'])  # Decorator for index URL route to webpage
def index():
    
    """index method simply returns the render template with the index html template. This template is actually a voter
    registration form."""
    
    date = datetime.now().strftime('%B/%d/%y')
    time = datetime.now().strftime('%I:%M%p')
    return render_template('index.html', time=time, date=date)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    name = ''
    email = ''
    phone = ''
    username = ''
    password = ''

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and \
            'email' in request.form and 'phone' in request.form:
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        username = request.form.get('username')
        password = request.form.get('password')

    if 6 < len(password) <= 16 and 5 < len(username) <= 14 and phone.isdigit():
        with open("users.txt", 'w') as users_file:
            for user in users:
                hashed_psw = sha256_crypt.hash(password).hexdigest()
                print([user], file=users_file)

    return render_template('signup.html', hashed_psw=hashed_psw, name=name, email=email,
                           phone=phone, username=username, password=password)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form.get('username')
        password = request.form.get('password')
        hash_psw = sha256_crypt.hash(password)

    with open("users.txt.txt", 'r') as users_file:
        contents = users_file.readline()
    user = eval(contents)
    print(user)
    # if psw_entered == password:

    return render_template('login.html', username=username, hash_psw=hash_psw)


if __name__ == '__main__':
    app.run(debug=True)  # Runs the flask app
