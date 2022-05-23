import psycopg2
from DataBaseTools.UserPortfolioTools import view_portfolio


# this function takes as input a ticker and returns a percentage that is the value at risk
def VaR_Stock(ticker):
    conn = psycopg2.connect(
        database="STEM", user='postgres',
        password='admin', host='localhost', port='5432')

    # getting last 500 stock price
    query = "select close from price where ticker ='{}' order by date desc limit 501".format(
        ticker)
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    price = []
    for i in range(len(data)):
        price.append(float(data[i][0]))

    # getting the percentage changes and sorting them in order
    PercentChange = []
    for i in range(len(price)-1):
        PercentChange.append(((price[i]-price[i+1]) / price[i+1])*100)
    PercentChange.sort()

    VaR = abs(PercentChange[4])
    return VaR


# this function calculates the VaR of each stock in the portfolio
def VaR_Portfolio_view(userId):
    df = view_portfolio(userId)
    VaR = []
    for index, row in df.iterrows():
        VaR.append(row['current_value']*VaR_Stock(row['ticker'])/100)
    df['VaR'] = VaR
    return df[['ticker', 'VaR']]


# this function calculates the value at risk from the entire portfolio
def VaR_Portfolio(userId):
    df = VaR_Portfolio_view(userId)
    VaR = 0
    for index, row in df.iterrows():
        VaR += row['VaR']
    return VaR


# calculates sum and total
def var_percent(userId):
    df = view_portfolio(userId)
    total = round(sum(df['current_value']), 2)
    return(total, round(100*VaR_Portfolio(userId)/total, 2))


# this function finds the stock with the highest value at risk  in the portfolio
def decrease_VaR_Portfolio(userId):
    df = VaR_Portfolio_view(userId)
    max = -1
    max_ticker = ""
    for index, row in df.iterrows():
        if row['VaR'] > max:
            max_ticker = row['ticker']
            max = row['VaR']
    return max_ticker
