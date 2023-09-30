import psycopg2

# database = mydb or postgres
# password = test123
connection = psycopg2.connect(
        host="localhost",
        database="",
        user="postgres",
        password=""
    )

connection.autocommit = True