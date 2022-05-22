import psycopg2
from getStockPrice import getStockPrice

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
    #get the last date
    date = df.iloc[-1]['Date']
    
    if (cash< price*quantity):
        raise Exception("Not Enough Cash")

    query = "Update usercash set cash = cash - "+str(price*quantity)+" where user_id = "+str(userId)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    query = "select count(*) from userportfolio where user_id ='{}' and ticker = '{}' and buy_date = '{}'".format(userId,ticker,date)
    cursor = conn.cursor()
    cursor.execute(query)
    count = cursor.fetchall()[0][0]
    if (count == 0):
        query = "Insert into userportfolio (user_id,ticker,buy_date,nb_shares) values ('{}','{}','{}','{}')".format(userId,ticker,date,quantity)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
    
    else:
        query = "Update userportfolio set nb_shares = nb_shares +{} where user_id ='{}' and ticker = '{}' and buy_date = '{}' ".format(quantity,userId,ticker,date)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()

buy_stock(1,'MMM',5)