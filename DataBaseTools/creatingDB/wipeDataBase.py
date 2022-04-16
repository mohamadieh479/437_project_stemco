import psycopg2
from .webScraping import getCompanies
"""
This code creates a table of the companies we have extracted using webScraping. The list we built in that code
is imported and it essentially contains the information / fields that make up the table.
"""

def wipeDataBase():
    # Connect to database
    conn = psycopg2.connect(
            database="STEM",user = 'postgres',
            password ='admin', host='localhost', port= '5432')

    # drop all tables.
    cursor=conn.cursor()
    cursor.execute("DROP TABLE if exists price CASCADE")
    cursor.execute("DROP TABLE if exists balancesheet CASCADE")
    cursor.execute("DROP TABLE if exists company CASCADE")
    cursor.execute("DROP TABLE if exists cashflowstatement CASCADE")
    cursor.execute("DROP TABLE if exists incomestatement CASCADE")
    conn.commit()
    cursor.close()        
    conn.close()

        

