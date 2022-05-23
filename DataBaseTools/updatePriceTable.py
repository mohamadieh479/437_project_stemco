import psycopg2
import datetime as dt
import pandas_datareader as web
"""
This file contains a function that updates the price table(getting the latest information)
"""
def updatePrices():
        #creating a connection with the database
        conn = psycopg2.connect(
                database="STEM",user = 'postgres',
                password ='admin', host='localhost', port= '5432')


        #finding the latest date in the database
        query = "select date from price order by date desc limit 1"

        cursor=conn.cursor()
        cursor.execute(query)
        try:
                date = cursor.fetchone()[0]
        except Exception:
                date = "2017-09-01"

        
        #extracting the year,month,day from date string
        year =int( date[0:4])
        month = int(date[5:7])
        day  = int(date[8:])

        #setting the start and end dates that will be extracted from the api
        start = dt.datetime(year=year,month=month,day=day)
        end = dt.datetime.now()
        delt=end-start
        if(delt<dt.timedelta(days=7)):
                conn.close()
                return None
        print("updating db, please wait a bit")
        #deleting the date to not have duplicate entries in database while inserting the new data
        query = "delete from price where date = '"+date+"'"
        cursor.execute(query)
        conn.commit()
        cursor.close()




        #inserting the new values into the database

        #getting the tickers of the companies from the company table
        query = "select ticker from company"
        cursor = conn.cursor()
        cursor.execute(query)
        tickers = cursor.fetchall()

        #looping over the tickers
        for ticker in tickers:
                #Load Data from the api for a given company
                data = web.DataReader(ticker[0], 'yahoo', start,end)
                # Restructure Data as we only need open high low close and volume
                data = data[['Open','High','Low','Close','Volume']]
                #changing the index from date to numerical. Date is no longer the index
                data.reset_index(inplace=True)
                try:    
                        #inserting the data in the database. each entry corresponds to a date
                        for i in range(len(data)-1):#the last element is not part of the needed data
                                print('-',end='')
                                cursor=conn.cursor()
                                s = str(data['Date'][i])[0:10]
                                volume = str(data['Volume'][i])
                                cursor.execute('''Insert into price (ticker,date,open,high,low,close,volume) values (%s,%s,%s,%s,%s,%s,%s)''',(ticker[0],s,data['Open'][i],data['High'][i],data['Low'][i],data['Close'][i],volume))
                                conn.commit()
                except Exception as e:
                        print(e)
        print()

        conn.close()

