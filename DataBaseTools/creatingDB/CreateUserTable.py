import psycopg2

def CreateUserTable():
    conn = psycopg2.connect(
            database="STEM",user = 'postgres',
            password ='admin', host='localhost', port= '5432')

    query = """Create table if not exists users(
        id SERIAL PRIMARY KEY,
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
        )"""
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()

    conn.close()