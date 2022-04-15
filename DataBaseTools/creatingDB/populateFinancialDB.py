import psycopg2
import requests
import time

"""
Tables are created. This code handles filling them using our API. Results are parsed and the
query is built up throughout the loop. The same procedure is followed for all three
financial statements.
"""


def populateFinancialDB():
    # Connect with database
    conn = psycopg2.connect(
            database="STEM",user = 'postgres',
            password ='admin', host='localhost', port= '5432')

    # Fetch all the tickers and store them as they are the primary keys
    query = "select ticker from company"
    cursor = conn.cursor()
    cursor.execute(query)
    tickers = cursor.fetchall()

    # Lets unsuccessful request retry for 5 times only. A successful request resets it back to five.
    count = 5

    # Populate the 'balancesheet' table
    # loop over every single company through its ticker, which is the primary key 
    for company in tickers:
        while count>=0:
            try:
                # Getting the balance sheet data from the api
                balance_sheet = requests.get(f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company[0]}?period=quarterly&limit=120&apikey=b4f84c6c34f5357de23599be344e76c2")
                # Extracting the data from the API (initially retrieved as a Response object)
                balance_sheet =balance_sheet.json() 
                counter = 0
                # API allows us to extract the balance sheet of the past five years, stored in 'balance_sheet'.
                for balance in balance_sheet: # balance is the balance sheet at a specific year of company x
                    # build query as we go; balance_sheet is shaped as a dictionary so loop through the keys (that were used before in createFinancialDataTable.py to create the table ensuring key match)
                    # note that ticker is added manually because it is not part of the Response object, rather an input we gave to the API
                    query = "insert into balancesheet values('"+company[0]+"','"
                    for key in balance.keys():
                        # make sure to wrap arguments in quotations
                        query+=str(balance[str(key)])+"','"
                    query=query[:-2] + ')' # loop adds an extra comma and closing quotation --> remove them.
                    cursor.execute(query)
                    conn.commit()
                count = 5 # if succesful, reset count (ie number of chances) back to 5
                break
            except Exception as e:
                # in case of error, usually fast request or request limit, let the system sleep for a while
                print(balance_sheet)
                time.sleep(0.2)
                count-=1

    # Populates the incomestatement table as done above
    for company in tickers:
        while count>=0:
            try:
                #getting the balance sheet data from the api
                income_statement = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{company[0]}?period=quarterly&limit=120&apikey=b4f84c6c34f5357de23599be344e76c2")
                #extracting the data from the api
                income_statement =income_statement.json()
                counter = 0
                for statement in income_statement: # statement is the cash flow statement at a specific year of company x
                    query = "insert into incomestatement values('"+company[0]+"','"
                    for key in statement.keys():
                        query+=str(statement[str(key)])+"','"
                    query=query[:-2] + ')'
                    cursor.execute(query)
                    conn.commit()
                count = 5
                break
            except Exception as e:
                print(income_statement)
                time.sleep(0.2)
                count-=1


    #populates the cashflowstatement table
    for company in tickers:
        while count>=0:
            try:
                #getting the balance sheet data from the api
                cash_flow_statement = requests.get(f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{company[0]}?period=quarterly&limit=120&apikey=b4f84c6c34f5357de23599be344e76c2")
                #extracting the data from the api
                cash_flow_statement = cash_flow_statement.json()
                counter = 0
                for statement in cash_flow_statement: # statement is the cash flow statement at a specific year of company x
                    query = "insert into cashflowstatement values('"+company[0]+"','"
                    for key in statement.keys():
                        query+=str(statement[str(key)])+"','"
                    query=query[:-2] + ')'
                    cursor.execute(query)
                    conn.commit()
                count = 5
                break
            except Exception as e:
                print(cash_flow_statement)
                time.sleep(0.2)
                count-=1


    cursor.close()

