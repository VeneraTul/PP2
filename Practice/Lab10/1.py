import psycopg2
import csv
from config1 import params

name1=input("whats your name?")

def create_table():
    SQL = ("""CREATE TABLE IF NOT EXISTS kniga(
           name VARCHAR(256) NOT NULL,
           phone VARCHAR(12) NOT NULL
    )""")

    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        query.close()
        config.commit()
    except Exception as Error:
        print(str(Error))

create_table()
def add_user(name,phone):
    SQL = (f'''INSERT INTO kniga(name,phone) VALUES = {name,phone})''')
    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        query.close()
        config.commit()
    except Exception as Error:
        print(str(Error))

def del_by_name():
    SQL = (f'''DELETE FROM kniga where name = {name1}''' )


#del_by_name(name1)