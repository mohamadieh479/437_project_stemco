import bs4 as bs
import requests
"""
Web Scraping code to get the name of all the companies, along with the ticker, name, exchange name, and industry type.
This construced list will be useful in other codes, particularly when building / interacting with the database.
"""

def getCompanies():

    # Retrieve the HTML page
    html = requests.get('https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average') # returns a Response object (200 ie succeeded)
    # To parse / read the object, use the beautiful soup library which extracts the HTML code from the response
    soup = bs.BeautifulSoup(html.text)

    companies = []

    # We don't need the whole html page, just the table of the DJIA companies. As such, retrieve this table only.
    table = soup.find('table', {'class':'wikitable sortable'})
    # First row of table lists the table heads / column titles. Select every other row to exclude it.
    rows = table.findAll('tr')[1:]

    # Columns are for<tr> : exchange,symbol,industry
    # Name is in <th>
    for row in rows:
        company=[] # "companies" will be a 2D array; "company" is the 1D array making up the former.
        # In the following, extract relevant titles. Indexing depends on the indexing of the table in the Wiki page.
        # getting the ticker
        ticker = row.findAll('td')[1].text
        company.append(ticker[:-1])
        # getting the name
        name = row.find('th').text
        company.append(name[:-1])
        # getting the exchange name
        ticker = row.findAll('td')[0].text
        company.append(ticker[:-1])
        # getting the industry type
        ticker = row.findAll('td')[2].text
        company.append(ticker[:-1])
        companies.append(company)
    return companies
    

