import psycopg2
from .webScraping import getCompanies
"""
This code creates a table of the companies we have extracted using webScraping. The list we built in that code
is imported and it essentially contains the information / fields that make up the table.
"""

def createDatabase():
    # Connect to database
    conn = psycopg2.connect(
            database="STEM",user = 'postgres',
            password ='admin', host='localhost', port= '5432')

    # Initialize the table, fields, and entry types.
    query = """Create table if not exists company(
        ticker varchar(5),
        name varchar(60),
        exchange varchar(60),
        industry varchar(60),
        primary key (ticker)
        )"""
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()

    # loop over all companies
    for entry in getCompanies():
        try:
        # entry is the 1D array (previously defined as 'company') that defines one company (ticker, name, exchange, industry)
            cursor=conn.cursor()
            # insert query to fill the created table
            cursor.execute('''Insert into company (ticker,name,exchange,industry) values (%s,%s,%s,%s)''',(entry[0],entry[1],entry[2],entry[3]))
            conn.commit()
        except Exception as e:
            print("Error message: ",e)
            
    conn.close()

        

