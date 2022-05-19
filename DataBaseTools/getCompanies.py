import pandas as pd
import psycopg2


def getCompanies():
    # connecting to the database
    conn = psycopg2.connect(
        database="STEM", user='postgres',
        password='admin', host='localhost', port='5432')

    query = "select name, ticker from company"
    cursor = conn.cursor()
    cursor.execute(query)
    nt = cursor.fetchall()
    # reformat into list for the selection feature
    select = [x + ' (%s)' % (y) for x, y in nt]
    tickers = [y for x, y in nt]
    select = zip(select, tickers)
    return select
