import psycopg2

connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="lh%4SWwB$cV4Xw"
    )

connection.autocommit = True