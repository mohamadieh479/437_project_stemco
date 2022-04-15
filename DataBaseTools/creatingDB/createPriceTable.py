import psycopg2
import datetime as dt
import pandas_datareader as web
"""
This code creates a table of the prices of the companies in the company table.
It includes the open,high,low,close prices and the volume traded in a given day.
"""

def createPriceTable():
    #connecting to the database
    conn = psycopg2.connect(
            database="STEM",user = 'postgres',
            password ='admin', host='localhost', port= '5432')

    # Initialize the table, fields, and entry types.
    query = """create table if not exists price (
        ticker varchar(5),
        date varchar(20),
        open varchar(20),
        high varchar (20),
        low varchar(20),
        close varchar(20),
        volume varchar(20),
        primary key (ticker,date),
        foreign key (ticker) references company)"""

    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()

    #pick the start and end times for retrieving the data
    #input for datetime is year,month,day
    start = dt.datetime(2021,9,1)
    end = dt.datetime.now()



    #getting the tickers from the company table in the database
    query = "select ticker from company"
    cursor = conn.cursor()
    cursor.execute(query)
    tickers = cursor.fetchall()

    # loop over all tickers
    for ticker in tickers:
        #Load Data from the yahoo api using the pandas_datareader library
        data = web.DataReader(ticker[0], 'yahoo', start,end)
        # Restructure Data as we only need open high low close and volume
        data = data[['Open','High','Low','Close','Volume']]
        #changing the index from date to numerical. Date is no longer the index
        data.reset_index(inplace=True)

        #inserting the data into the database
        try:
            for i in range(len(data)-1):#the last element is nor part of the needed data 
                cursor=conn.cursor()
                s = str(data['Date'][i])[0:10] #reformating the date to fit in our database
                volume = str(data['Volume'][i]) #reformating the volume to avoid problems with the api
                cursor.execute('''Insert into price (ticker,date,open,high,low,close,volume) values (%s,%s,%s,%s,%s,%s,%s)''',(ticker[0],s,data['Open'][i],data['High'][i],data['Low'][i],data['Close'][i],volume))
                conn.commit()
        except Exception as e:
            print(e)