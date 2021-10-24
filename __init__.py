from flask import Blueprint, render_template, request, flash, redirect, url_for
from sqlalchemy.sql.functions import current_user
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
#hash is a one way function such that it does not have an inverse...this secures
#the password

auth = Blueprint('auth', __name__)

@auth.route('/')
def home():
    return render_template('home.html', user = current_user)

#the belwo creates different pages with different urls in webb app
@auth.route('/login', methods = ['GET', 'POST'])

#get requests loads information
#POST request means you are making a change to a data base
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        #filter the database for the email that corresponds to the 
        #login email (one to one correspondence)
        if user:
            if check_password_hash(user.password, password):
                #second paramter cheecks to see if input password matches data 
                #base password
                flash('Logged in Successfully!', category = 'success') 
                login_user(user, remember=True)
                return redirect(url_for('views.note'))
            else: 
                flash("Incorrect password, please try again.", category = 'error')
        else:
            flash('Email does not exist.', category = 'error')

    #data = request.form
    #print(data)
    return render_template("login.html",user = current_user)
        
    #you can assign a variable name (and call it) as done above when using
    #the varibale text (its paramter,testing coudl've been ANYTHING),
    #"Testing" IS the evalue of the varibale text,
    #the value of text can be displayed between the {{}} in 
    #login.html

@auth.route('/logout')
#this allows us to load (get) the information on a page as 
#and store the information submitted/actions performed in the web app database
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/graphs')
@login_required
def graphs():
    return render_template('graphs.html', user = current_user)


@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    
    #the iff statment below gets and stores the information
    #put in the sign up form into a datbase
    #Notice is stores email by requesting and getting the email parameter
    #in the login.html
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category = 'error')
            #let's make sure the inputs are valid
        elif len(email) < 4:
            #tells the user the status of their input (was it valid or not)
            #the category paramter can be set to error (for failure/invalid input)
            #it can also be set to success (for valid input)
            flash('Email must be greater than 4 characters.', category = 'error')
            pass
        elif len(first_name) < 2:
            flash('First name must be greater than 2 characters.', category = 'error')
            pass
        elif password1 != password2:
            flash('Passwords don\'t match.', category = 'error')
            pass
        elif len(password1) < 7:
            flash('Passoword must be greater than 7 characters.', category = 'error')
            pass
        else:
            #add user to database
            new_user = User(email=email,first_name=first_name,password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            #updates the data base
            login_user(new_user, remember=True)
            flash('Account created!', category = 'success')
            return redirect(url_for('views.note'))
