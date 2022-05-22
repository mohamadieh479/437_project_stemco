import click
from flask.cli import with_appcontext

from . import createFinancialDataTable,createPriceTable,populateFinancialDB,\
                createDatabase,wipeDataBase,CreateUserTable,createUserPortfolioTable

@click.command('init-db')
@with_appcontext
def init_db_command():
    wipeDataBase.wipeDataBase()
    click.echo('process 1/7 done')
    createDatabase.createDatabase()
    click.echo('process 2/7 done')
    createPriceTable.createPriceTable()
    click.echo('process 3/7 done')
    createFinancialDataTable.createFinancialDataTable()
    click.echo('process 4/7 done')
    CreateUserTable.CreateUserTable()
    click.echo('process 5/7 done')
    createUserPortfolioTable.createUserPortfolioTable()
    createUserPortfolioTable.createUserCashTable()
    click.echo('process 6/7 done')
    populateFinancialDB.populateFinancialDB()
    click.echo('Initialized the database.')