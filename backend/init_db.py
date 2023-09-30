import psycopg2

def setup():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="")

    #create a cursor to execute sql database commands
    cursor = conn.cursor()

    conn.autocommit = True

    #delete preexisting mydb if it conflicts with current mydb
    cursor.execute('''DROP DATABASE IF EXISTS mydb''')

    #Preparing query to create a database
    sql = '''CREATE database mydb;''';

    #Creating a database
    cursor.execute(sql)
    print("Database created successfully........")

    #Closing the connection
    conn.close()    

setup()