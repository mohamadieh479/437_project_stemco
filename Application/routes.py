from Application import app
from flask import render_template,request,session,g,redirect,url_for
import functools

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    if request.method == 'POST':
        pass

    return render_template("login.html")

@app.route("/register")
def register():
    if request.method == 'POST':
        pass

    return render_template("register.html")



#The following functions will likely be relocated
@app.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        #TODO function to load user
        pass

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('login'))

        return view(**kwargs)
    return wrapped_view