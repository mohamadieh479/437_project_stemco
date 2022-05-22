import psycopg2

def createUserPortfolioTable():
    conn = psycopg2.connect(
            database="STEM",user = 'postgres',
            password ='admin', host='localhost', port= '5432')

    query = """Create table if not exists userportfolio(
        user_id SERIAL not NULL,
        ticker varchar(5) NOT NULL,
        nb_shares int NOT NULL,
        primary key(user_id,ticker),
        foreign key(user_id) references users
		on delete cascade,
        foreign key(ticker) references company
        )"""
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()

    conn.close()


def createUserCashTable():
    conn = psycopg2.connect(
            database="STEM",user = 'postgres',
            password ='admin', host='localhost', port= '5432')

    #date must be inserted in the format year-month-day to conform with the price table
    query = """Create table if not exists usercash(
        user_id SERIAL not NULL,
        cash BIGINT,
        primary key(user_id),
        foreign key(user_id) references users
		on delete cascade
        )"""
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
