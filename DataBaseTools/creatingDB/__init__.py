import click
from flask.cli import with_appcontext

from . import createFinancialDataTable,createPriceTable,populateFinancialDB,\
                createDatabase,wipeDataBase

@click.command('init-db')
@with_appcontext
def init_db_command():
    wipeDataBase.wipeDataBase()
    click.echo('process 1/5 done')
    createDatabase.createDatabase()
    click.echo('process 2/5 done')
    createPriceTable.createPriceTable()
    click.echo('process 3/5 done')
    createFinancialDataTable.createFinancialDataTable()
    click.echo('process 4/5 done')
    populateFinancialDB.populateFinancialDB()
    click.echo('Initialized the database.')