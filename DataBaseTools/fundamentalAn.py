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


#this function returns a dataframe of the  QuickRatio of a company for the last 5 years
#The dataframe has 2 columns 'Date' and 'QuickRatio'
#This function takes as input the ticker of a company
def QuickRatio(ticker):
    conn = psycopg2.connect(
            database="STEM",user = 'postgres',
            password ='admin', host='localhost', port= '5432')
    
    query = "select date,totalcurrentassets,inventory,totalcurrentliabilities from balancesheet where ticker ='"+ticker+"' order by date ASC "
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    col = ['Date','totalcurrentassets','inventory','totalcurrentliabilities']
    df = pd.DataFrame(data,columns=col)
    df['totalcurrentassets'] =pd.to_numeric(df['totalcurrentassets'])
    df['totalcurrentliabilities'] =pd.to_numeric(df['totalcurrentliabilities'])
    df['inventory'] =pd.to_numeric(df['inventory'])

    QuickRatio = []
    QuickRatio.append((df['totalcurrentassets'][0]-df['inventory'][0])/df['totalcurrentliabilities'][0])
    QuickRatio.append((df['totalcurrentassets'][1]-df['inventory'][1])/df['totalcurrentliabilities'][1])
    QuickRatio.append((df['totalcurrentassets'][2]-df['inventory'][2])/df['totalcurrentliabilities'][2])
    QuickRatio.append((df['totalcurrentassets'][3]-df['inventory'][3])/df['totalcurrentliabilities'][3])
    QuickRatio.append((df['totalcurrentassets'][4]-df['inventory'][4])/df['totalcurrentliabilities'][4])
    df['QuickRatio'] = QuickRatio
    return df[['Date','QuickRatio']]



#this function returns a dataframe of the WorkingCapitalRatio of a company for the last 5 years
#The dataframe has 2 columns 'Date' and 'WorkingCapitalRatio'
#This function takes as input the ticker of a company
def WorkingCapitalRatio(ticker):
    conn = psycopg2.connect(
            database="STEM",user = 'postgres',
            password ='admin', host='localhost', port= '5432')
    
    query = "select date,totalcurrentassets,totalcurrentliabilities from balancesheet where ticker ='"+ticker+"' order by date ASC "
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    col = ['Date','totalcurrentassets','totalcurrentliabilities']
    df = pd.DataFrame(data,columns=col)
    df['totalcurrentassets'] =pd.to_numeric(df['totalcurrentassets'])
    df['totalcurrentliabilities'] =pd.to_numeric(df['totalcurrentliabilities'])

    WorkingCapitalRatio = []
    WorkingCapitalRatio.append((df['totalcurrentassets'][0])/df['totalcurrentliabilities'][0])
    WorkingCapitalRatio.append((df['totalcurrentassets'][1])/df['totalcurrentliabilities'][1])
    WorkingCapitalRatio.append((df['totalcurrentassets'][2])/df['totalcurrentliabilities'][2])
    WorkingCapitalRatio.append((df['totalcurrentassets'][3])/df['totalcurrentliabilities'][3])
    WorkingCapitalRatio.append((df['totalcurrentassets'][4])/df['totalcurrentliabilities'][4])
    df['WorkingCapitalRatio'] = WorkingCapitalRatio
    return df[['Date','WorkingCapitalRatio']]



#this function returns a dataframe of the return on equity of a company for the last 5 years
#The dataframe has 2 columns 'Date' and 'ROE'
#This function takes as input the ticker of a company
def ROE(ticker):
    conn = psycopg2.connect(
            database="STEM",user = 'postgres',
            password ='admin', host='localhost', port= '5432')
    
    query = """select b.date,totalstockholdersequity,netincome from balancesheet b join cashflowstatement c on b.ticker = c.ticker and b.date=c.date
where b.ticker= '"""+ticker+"""' order by date ASC """
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    col = ['Date','totalstockholdersequity','netincome']
    df = pd.DataFrame(data,columns=col)
    df['totalstockholdersequity'] =pd.to_numeric(df['totalstockholdersequity'])
    df['netincome'] =pd.to_numeric(df['netincome'])
    ROE = []
    ROE.append(df['netincome'][0]/(df['totalstockholdersequity'][0]))
    ROE.append(df['netincome'][1]/(df['totalstockholdersequity'][1]))
    ROE.append(df['netincome'][2]/(df['totalstockholdersequity'][2]))
    ROE.append(df['netincome'][3]/(df['totalstockholdersequity'][3]))
    ROE.append(df['netincome'][4]/(df['totalstockholdersequity'][4]))
    df['ROE'] = ROE
    return df[['Date','ROE']]
