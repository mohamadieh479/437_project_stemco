from asyncio.windows_events import NULL
from sysconfig import get_path_names
from DataBaseTools import UserTableTools,UserPortfolioTools
from werkzeug.security import check_password_hash, generate_password_hash
from flask import g,redirect,url_for,flash
import functools

class User():
    def __init__(this):
        this.__data = NULL

    def load_user_id(this,id):
        this.__data = UserTableTools.fetch_user_ID(id)
        if(this.__data is None):
            this.__data = NULL
            return False
        return True

    def login(this,username,password):
        
        data = UserTableTools.fetch_user_USERNAME(username)

        if(data is None or not check_password_hash(data[5], password)):
            return False
        
        this.__data = data

        return True

    def register(this,firstname,lastname,username,email,password):

        if(UserTableTools.fetch_user_USERNAME(username) is not None):
            flash("username already exists","error")
            return False
        if(UserTableTools.check_user_email_exists(email)):
            flash("email already exists","error")
            return  False
        UserTableTools.add_user(firstname,lastname,username,email,generate_password_hash(password))
        response = this.login(username,password)
        if(response):
            UserPortfolioTools.init_cash(this.get_id)
        return response
        


    def get_id(this):
        assert this.__data != NULL, "User object corresponds to no existing user"

        return this.__data[0]

    def get_username(this):
        assert this.__data != NULL, "User object corresponds to no existing user"

        return this.__data[3]
        
    def get_firsname(this):
        assert this.__data != NULL, "User object corresponds to no existing user"

        return this.__data[1]

    def get_lastname(this):
        assert this.__data != NULL, "User object corresponds to no existing user"

        return this.__data[2]

    def get_email(this):
        assert this.__data != NULL, "User object corresponds to no existing user"

        return this.__data[4]

def login_required(view): # add '@login_required' before any function (and after route) to force the user to login first
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('login'))

        return view(**kwargs)
    return wrapped_view
