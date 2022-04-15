import click
from flask.cli import with_appcontext

from . import createFinancialDataTable,createPriceTable,populateFinancialDB,createDatabase,updatePriceTable

@click.command('init-db')
@with_appcontext
def init_db_command():
    #add a function to drop all tables
    createDatabase.createDatabase()
    createPriceTable.createPriceTable()
    updatePriceTable.updatePrices()
    createFinancialDataTable.createFinancialDataTable()
    populateFinancialDB.populateFinancialDB()
    click.echo('Initialized the database.')