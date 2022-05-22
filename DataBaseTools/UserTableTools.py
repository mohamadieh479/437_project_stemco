import psycopg2
from DataBaseTools.UserPortfolioTools import init_cash
def add_user(firstname,lastname,username,email,password):
    conn = psycopg2.connect(
            database="STEM",user = 'postgres',
            password ='admin', host='localhost', port= '5432')

    query = "Insert into users (firstname,lastname,username,email,password) values ('{}','{}','{}','{}','{}')".format(firstname,lastname,username,email,password)
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()

    conn.close()


def fetch_user_ID(id):
    #TODO: error handling
    conn = psycopg2.connect(
            database="STEM",user = 'postgres',
            password ='admin', host='localhost', port= '5432')

    query = "SELECT * FROM users WHERE id = '{}'".format(id)
    cursor=conn.cursor()
    cursor.execute(query)
    user_data = cursor.fetchone()
    cursor.close()

    conn.close()

    return user_data

def fetch_user_USERNAME(username):
    conn = psycopg2.connect(
            database="STEM",user = 'postgres',
            password ='admin', host='localhost', port= '5432')

    query = "SELECT * FROM users WHERE username = '{}'".format(username)
    cursor=conn.cursor()
    cursor.execute(query)
    user_data = cursor.fetchone()
    cursor.close()

    conn.close()

    return user_data

def update_user(id,firstname,lastname,email,password):
    conn = psycopg2.connect(
            database="STEM",user = 'postgres',
            password ='admin', host='localhost', port= '5432')

    query = "UPDATE users SET firstname = '{}', lastname = '{}', email = '{}', password = '{}' WHERE id = '{}'".format(firstname,lastname,email,password,id)
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()

    conn.close()

def check_user_email_exists(email):
    conn = psycopg2.connect(
            database="STEM",user = 'postgres',
            password ='admin', host='localhost', port= '5432')

    query = "SELECT * FROM users WHERE email = '{}'".format(email)
    cursor=conn.cursor()
    cursor.execute(query)
    user_data = cursor.fetchone()
    cursor.close()

    conn.close()

    return user_data is not None