import psycopg2
import requests


def createFinancialDataTable():
    conn = psycopg2.connect(
            database="STEM",user = 'postgres',
            password ='admin', host='localhost', port= '5432')

    #choosing a random company
    company = "FB"

    #getting the balance sheet data from the api
    balance_sheet = requests.get(f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company}?period=quarterly&limit=120&apikey=b4f84c6c34f5357de23599be344e76c2")

    #extracting the data from the api
    balance_sheet =balance_sheet.json()

    #creating the balance sheet table
    query = "create table if not exists BalanceSheet(ticker varchar(5),"
    for key in balance_sheet[0].keys():
        query+= str(key)+ " varchar(105),"
    query  += "primary key (ticker,date), foreign key (ticker) references company)"

    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()


    #getting the income-statement data from the api
    income_statement = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?period=quarterly&limit=120&apikey=b4f84c6c34f5357de23599be344e76c2")
    #extracting the data from the api
    income_statement =income_statement.json()

    #creating the income statement table

    query = "create table IncomeStatement(ticker varchar(5),"
    for key in income_statement[0].keys():
        query+= str(key)+ " varchar(105),"
    query  += "primary key (ticker,date), foreign key (ticker) references company)"


    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()




    #getting the cash-flow-statement data from the api
    cash_flow_statement = requests.get(f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{company}?period=quarterly&limit=120&apikey=b4f84c6c34f5357de23599be344e76c2")
    #extracting the data from the api
    cash_flow_statement =cash_flow_statement.json()
    #creating the cashflow statement table

    query = "create table CashFlowStatement(ticker varchar(5),"
    for key in cash_flow_statement[0].keys():
        query+= str(key)+ " varchar(105),"
    query  += "primary key (ticker,date), foreign key (ticker) references company)"

    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
