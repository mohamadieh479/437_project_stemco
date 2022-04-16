import pandas as pd
import psycopg2


def getStockPrice(ticker):
    #connecting to the database
    conn = psycopg2.connect(
            database="STEM",user = 'postgres',
            password ='admin', host='localhost', port= '5432')

    query = "select date,open,high,low,close,volume from price where ticker = '"+ticker+"'" 
    cursor = conn.cursor()
    cursor.execute(query)
    price = cursor.fetchall()

    #creating a dataframe that will be used by the technical indicators library
    col =['Date','Open','High','Low','Close','Volume'] #defining the column name
    df=pd.DataFrame(price,columns=col)

    #converting the data from string to numeric in the dataframe
    df['Open'] = pd.to_numeric(df['Open'])
    df['High'] = pd.to_numeric(df['High'])
    df['Low'] = pd.to_numeric(df['Low'])
    df['Close'] = pd.to_numeric(df['Close'])
    df['Volume'] = pd.to_numeric(df['Volume'])
    return df
    