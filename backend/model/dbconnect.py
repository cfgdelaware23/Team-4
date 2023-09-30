import psycopg2

connection = psycopg2.connect(
        host="localhost",
        database="mydb",
        user="postgres",
        password="test123"
    )

connection.autocommit = True