import pandas as pd
import psycopg2


#This function returns a dataframe of the EPS of a company for the last 5 years
#The dataframe has 2 columns 'Date' and 'EPS'
#This function takes as input the ticker of a company
def EPS(ticker):
        conn = psycopg2.connect(
            database="STEM",user = 'postgres',
            password ='admin', host='localhost', port= '5432')
        query= "select date,eps from incomestatement where ticker ='"+ticker+"' order by date ASC"
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        col =['Date','EPS'] #defining the column name
        df=pd.DataFrame(data,columns=col)
        df['EPS'] = pd.to_numeric(df['EPS'])
        return df

#this function returns a dataframe of the PE ratio of a company for the last 5 years
#The dataframe has 2 columns 'Date' and 'PE'
#This function takes as input the ticker of a company
def PE(ticker):
        conn = psycopg2.connect(
            database="STEM",user = 'postgres',
            password ='admin', host='localhost', port= '5432')

        #getting the EPS
        query = "select date,eps from incomestatement where ticker ='"+ticker+"' order by date ASC "
        cursor = conn.cursor()
        cursor.execute(query)
        EPS = cursor.fetchall()

        #getting the latest stock price
        query = "select close,date from price where ticker ='"+ticker+"' order by date DESC limit 1"
        cursor = conn.cursor()
        cursor.execute(query)
        Price2021 = float(cursor.fetchall()[0][0])
        
        #getting the price of 2020
        query = "select close,date from price where ticker = '"+ticker+"' and date like '2020-12%'order by date DESC limit 1"
        cursor = conn.cursor()
        cursor.execute(query)
        Price2020 = float(cursor.fetchall()[0][0])
        
        #getting the price of 2019
        query = "select close,date from price where ticker = '"+ticker+"' and date like '2019-12%'order by date DESC limit 1"
        cursor = conn.cursor()
        cursor.execute(query)
        Price2019 = float(cursor.fetchall()[0][0])

        #getting the price of 2018
        query = "select close,date from price where ticker = '"+ticker+"' and date like '2018-12%'order by date DESC limit 1"
        cursor = conn.cursor()
        cursor.execute(query)
        Price2018 = float(cursor.fetchall()[0][0])

        #getting the price of 2017
        query = "select close,date from price where ticker = '"+ticker+"' and date like '2017-12%'order by date DESC limit 1"
        cursor = conn.cursor()
        cursor.execute(query)
        Price2017 = float(cursor.fetchall()[0][0])

        col =['Date','EPS'] #defining the column name
        df=pd.DataFrame(EPS,columns=col)
        df['EPS'] = pd.to_numeric(df['EPS'])


        PE = []
        PE.append(Price2017/df['EPS'][0])
        PE.append(Price2018/df['EPS'][1])
        PE.append(Price2019/df['EPS'][2])
        PE.append(Price2020/df['EPS'][3])
        PE.append(Price2021/df['EPS'][4])
        df['PE'] = PE
        return df[['Date','PE']]