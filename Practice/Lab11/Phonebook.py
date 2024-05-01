import psycopg2 
from config import params 
import csv 
import re 
 
a = int(input('1-Add     2-Delete     3-Update     4-Show     5-csv      6-find   7-pagination \n')) 
 
def create_table(): 
    SQL = ( 
        ''' 
        CREATE TABLE IF NOT EXISTS phonebook2 (  
        Name VARCHAR(255) NOT NULL ,  
        number VARCHAR(11) NOT NULL 
    )  
        ''' 
    ) 
 
    try: 
        config = psycopg2.connect(**params) 
        query = config.cursor() 
        query.execute(SQL) 
        query.close() 
        config.commit() 
 
    except Exception as Error: 
        print(str(Error)) 
 
create_table() 
 
def add_user(name, telephone): 
    SQL = "Select * from phonebook2 where name = '" + name + "';" 
    t = True 
    try: 
        config = psycopg2.connect(**params) 
        query = config.cursor() 
        query.execute(SQL) 
        res = query.fetchall() 
        query.close() 
        config.commit() 
 
        if len(res) != 0: 
            SQL = "UPDATE phonebook2 SET number = '" + telephone + "' WHERE name = '" + name + "';" 
            update(SQL) 
            t = False 
 
    except Exception as Error: 
        print(str(Error)) 
 
    if t: 
        SQL = "INSERT INTO phonebook2 (Name, number) VALUES ('" + name + "','" + telephone + "');" 
        try: 
            config = psycopg2.connect(**params) 
            query = config.cursor() 
            query.execute(SQL) 
            query.close() 
            config.commit() 
 
        except Exception as Error: 
            print(str(Error)) 
 
def drop(SQL): 
    try: 
        config = psycopg2.connect(**params) 
        query = config.cursor() 
        query.execute(SQL) 
        query.close() 
        config.commit() 
 
    except Exception as Error: 
        print(str(Error)) 
 
def update(SQL): 
    try: 
        config = psycopg2.connect(**params) 
        query = config.cursor() 
        query.execute(SQL) 
        query.close() 
        config.commit() 
 
    except Exception as Error: 
        print(str(Error)) 
 
def show(SQL, page): 
    SQL += " OFFSET " + str((int(page) - 1) * 3) + " ROWS FETCH NEXT 3 ROWS ONLY" 
 
    try: 
        config = psycopg2.connect(**params) 
        query = config.cursor() 
        query.execute(SQL) 
        res = query.fetchall() 
        query.close() 
        config.commit() 
 
        if len(res) != 0: 
            text = "Name                     Telephone" 
            print("\033[36m {}".format(text)) 
            print("\033[0m", end='') 
 
            for row in res: 
                l = len(row[0]) 
                print(str(row[0]), end="") 
                for i in range(24 - l): 
                    print(' ', end="") 
                print(' ', end="") 
                print(str(row[1])) 
 
        else: 
            print("\033[31m {}".format('Nothing found!')) 
        print("\033[0m", end='') 
 
    except Exception as Error: 
        print(str(Error)) 
 
def find(SQL): 
    try: 
        config = psycopg2.connect(**params) 
        query = config.cursor() 
        query.execute(SQL) 
        res = query.fetchall() 
        query.close() 
        config.commit() 
 
        if len(res) != 0: 
            text = "Name                     Telephone" 
            print("\033[36m {}".format(text)) 
            print("\033[0m", end='') 
 
            for row in res: 
                l = len(row[0]) 
                print(str(row[0]), end="") 
                for i in range(24 - l): 
                    print(' ', end="") 
                print(' ', end="") 
                print(str(row[1])) 
 
        else: 
            print("\033[31m {}".format('Nothing found!')) 
            print("\033[0m", end='') 
 
    except Exception as Error: 
        print(str(Error)) 

def get_data_with_pagination(limit, offset):
    try:
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        query = f"SELECT * FROM phonebook2 LIMIT {limit} OFFSET {offset};"

        cursor.execute(query)

    
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results

    except Exception as Error:
        print(str(Error)) 

 
if a == 1: 
    name = input('Write your name:   ') 
    telephone = input('Write your telephone number:   ') 
    add_user(name, telephone) 
 
if a == 2:

    b = int(input('1-Delete by name     2-Delete by telephone \n')) 
    if b == 1: 
        name = input('Write your name:     ') 
        SQL = "DELETE FROM phonebook2 where name = '" + name + "';" 
    if b == 2: 
        telephone = input('Write your telephone number:     ') 
        SQL = "DELETE FROM phonebook2 where telephone = '" + telephone + "';" 
 
    drop(SQL) 
 
if a == 3: 
    b = int(input('1-Update by name     2-Update by telephone \n')) 
    if b == 1: 
        name = input('Write your name:     ') 
        telephone = input('Write your new telephone number:     ') 
        SQL = "UPDATE phonebook2 SET number = '" + telephone + "' WHERE name = '" + name + "';" 
    if b == 2: 
        telephone = input('Write your telephone number: ') 
        name = input('Write your new name:     ') 
        SQL = "UPDATE phonebook2 SET name = '" + name + "' WHERE number = '" + telephone + "';" 
    update(SQL) 
 
if a == 4: 
    b = int(input('1-Sort by name     2-Sort by telephone     3-Sort by date\n')) 
    if b == 1: 
        SQL = 'Select * from phonebook2 order by name ASC' 
    if b == 2: 
        SQL = 'Select * from phonebook2 order by telephone ASC' 
    if b == 3: 
        SQL = '' 
    print("Print 'stop', to stop pagination.") 
    page = '' 
    while page != 'stop': 
        page = input('Write the page number: \n') 
        show(SQL, page) 
 
if a == 5: 
    with open('pb.csv') as f: 
        r = csv.reader(f) 
        for i in r: 
            name = str(i[0]) 
            telephone = str(i[1]) 
            add_user(name, telephone) 
 
if a == 6: 
    b = int(input('1-Find by name     2-Find by telephone\n')) 
    if b == 1: 
        name = input("Write your name:\n") 
        SQL = "SELECT * FROM phonebook2 where name LIKE '" + str(name) + "%';" 
    if b == 2: 
        telephone = input("Write your telephone:\n") 
        SQL = "SELECT * FROM phonebook2 where telephone LIKE '" + str(telephone) + "%';" 
    find(SQL)

if a == 7:
    limit = int(input())
    offset = int(input())
    results = get_data_with_pagination(limit, offset)
    for row in results:
       print(row)