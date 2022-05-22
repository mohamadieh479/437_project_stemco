from Analysis.technicalAn import BB_recommendation, MA_recommendation,EMA_recommendation,  RSI_recommendation
from DataBaseTools.UserPortfolioTools import view_portfolio


#this function takes as input a ticker and returns a recommendation on buying or selling a stock
def recommendation_stock(ticker):
    result = BB_recommendation(ticker) + 0.5*MA_recommendation(ticker) + 0.5*EMA_recommendation(ticker) + RSI_recommendation(ticker)
    if (result==3):
        return "Strong Buy"
    elif (result>=1):
        return "Buy"
    elif(result==-3):
        return "Strong Sell"
    elif (result<=-1):
        return "Sell"
    else:
        return "Neutral"


def recommendation_portfolio(userId):
    df = view_portfolio(userId)
    recommendation = []
    for index,row in df.iterrows():
        recommendation.append(recommendation_stock(row['ticker']))
    df['recommendation'] = recommendation
    return df[['ticker','recommendation']]
