import click
from flask.cli import with_appcontext

from . import createFinancialDataTable,createPriceTable,populateFinancialDB,\
                createDatabase,wipeDataBase,CreateUserTable

@click.command('init-db')
@with_appcontext
def init_db_command():
    wipeDataBase.wipeDataBase()
    click.echo('process 1/6 done')
    createDatabase.createDatabase()
    click.echo('process 2/6 done')
    createPriceTable.createPriceTable()
    click.echo('process 3/6 done')
    createFinancialDataTable.createFinancialDataTable()
    click.echo('process 4/6 done')
    CreateUserTable.CreateUserTable()
    click.echo('process 5/6 done')
    populateFinancialDB.populateFinancialDB()
    click.echo('Initialized the database.')