import psycopg2
from getStockPrice import getStockPrice
import pandas as pd


#this function will initialize the cash of new users to 0
def init_cash(username,password):
    conn = psycopg2.connect(
        database="STEM", user='postgres',
        password='admin', host='localhost', port='5432')
    
    query = "select id from users where username = '{}' and password='{}'".format(username,password)
    cursor = conn.cursor()
    cursor.execute(query)
    id = cursor.fetchall()[0][0]
    
    query="insert into usercash values({},0)".format(id)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


#this function updates the cash of the new users
def set_cash(userID,cash):
    conn = psycopg2.connect(
        database="STEM", user='postgres',
        password='admin', host='localhost', port='5432')

    query = "update usercash set cash ={} where user_id = {}".format(cash,userID)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def get_cash(userId):
    conn = psycopg2.connect(
        database="STEM", user='postgres',
        password='admin', host='localhost', port='5432')

    query = "select cash from usercash where user_id = '"+str(userId)+"'"
    cursor = conn.cursor()
    cursor.execute(query)
    cash = cursor.fetchall()[0][0]

    return cash

#this function will add a number of stocks of a given company to a users portfolio. It will raise an exception if the cash of the user isn't enough
def buy_stock(userId,ticker,quantity):
    conn = psycopg2.connect(
        database="STEM", user='postgres',
        password='admin', host='localhost', port='5432')

    query = "select cash from usercash where user_id = '"+str(userId)+"'"
    cursor = conn.cursor()
    cursor.execute(query)
    cash = cursor.fetchall()[0][0]

    df = getStockPrice(ticker)
    #get the last close price
    price = df.iloc[-1]['Close']
    
    
    if (cash< price*quantity):
        raise Exception("Not Enough Cash")

    query = "Update usercash set cash = cash - "+str(price*quantity)+" where user_id = "+str(userId)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    query = "select count(*) from userportfolio where user_id ='{}' and ticker = '{}'".format(userId,ticker)
    cursor = conn.cursor()
    cursor.execute(query)
    count = cursor.fetchall()[0][0]
    if (count == 0):
        query = "Insert into userportfolio (user_id,ticker,nb_shares) values ('{}','{}','{}')".format(userId,ticker,quantity)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
    
    else:
        query = "Update userportfolio set nb_shares = nb_shares +{} where user_id ='{}' and ticker = '{}' ".format(quantity,userId,ticker)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()


#this function will sell a number of stocks of a given company from a users portfolio. It will raise an exception if the quanitity sold 
#is more than the ones the user has(or if he doesn't own any).
def sell_stock(userId,ticker,quantity):
    conn = psycopg2.connect(
        database="STEM", user='postgres',
        password='admin', host='localhost', port='5432')

    df = getStockPrice(ticker)
    #get the last close price
    price = df.iloc[-1]['Close']

    query = "select count(*) from userportfolio where user_id ='{}' and ticker = '{}'".format(userId,ticker)
    cursor = conn.cursor()
    cursor.execute(query)
    count = cursor.fetchall()[0][0]

    if count==0:
        raise Exception("User doesn't have that stock")

    query = "select nb_shares from userportfolio where user_id ='{}' and ticker = '{}'".format(userId,ticker)
    cursor = conn.cursor()
    cursor.execute(query)
    nb_shares = cursor.fetchall()[0][0]
    if nb_shares<quantity:
        raise Exception("User doesn't have that quantity of shares")

    elif nb_shares==quantity:
        query="delete from userportfolio where user_id ='{}' and ticker = '{}'".format(userId,ticker)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()

        query = "Update usercash set cash = cash + "+str(price*quantity)+" where user_id = "+str(userId)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
    
    else:
        query = "Update userportfolio set nb_shares = nb_shares -{} where user_id ='{}' and ticker = '{}' ".format(quantity,userId,ticker)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()

        query = "Update usercash set cash = cash + "+str(price*quantity)+" where user_id = "+str(userId)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()


#this function takes as input userId and returns a dataframe showing what stocks the user owns and their values
def view_portfolio(userId):
    conn = psycopg2.connect(
        database="STEM", user='postgres',
        password='admin', host='localhost', port='5432')
    
    query ="select ticker,nb_shares from userportfolio where user_id = {}".format(userId)
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()

    col = ['ticker','nb_shares']  # defining the column name
    df = pd.DataFrame(data, columns=col)
    
    values=[]
    for index, row in df.iterrows():
        prices = getStockPrice(row['ticker'])
        #get the last close price
        price = prices.iloc[-1]['Close']
        values.append(row['nb_shares']*price)

    df['current_value'] = values
    return df

