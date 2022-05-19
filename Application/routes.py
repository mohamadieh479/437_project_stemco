from DataBaseTools.getStockPrice import getStockPrice
from Application import app
from flask import render_template, request, session, g, redirect, url_for, flash
from User import User, login_required

from DataBaseTools.getCompanies import getCompanies

@app.route("/")
# @login_required    #by uncommenting this,you can force user to sign in to access this page
def index():
    select = getCompanies()
    return render_template("index.html", options1=select)


@app.route("/login", methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['pass']

        user = User()
        if(user.login(username, password)):
            session.clear()
            session['user_id'] = user.get_id()
            return redirect(url_for('index'))
        else:
            flash("Incorrect username or password", "error")

    return render_template("login.html")


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route("/register", methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        passCheck = request.form['password2']
        firstname = request.form['fname']
        lastname = request.form['lname']
        email = request.form['email']

        user = User()

        if(password != passCheck):
            flash("Passwords don't match", "error")
        elif(user.register(firstname, lastname, username, email, password)):
            session.clear()
            session['user_id'] = user.get_id()
            return redirect(url_for('index'))

    return render_template("register.html")

# this means this function will run before all other route functions( suppose you open index page, this runs then the index function runs)


@app.before_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User()
        g.user.load_user_id(user_id)
