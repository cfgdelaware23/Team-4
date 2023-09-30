import psycopg2

connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password=""
    )

connection.autocommit = True