from dbconnect import connection

def setup():

    # Check if mydb database exists
    # cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'mydb';")
    # db_exists = cursor.fetchone() is not None

    # if not db_exists:
    #     # Creating a database
    #     cursor.execute('CREATE DATABASE mydb;')
    

    # Close connection to default postgres database
    # cursor.close()
    # connection.close()

    # # Connect to mydb database
    # connection = psycopg2.connect(
    #     host="localhost",
    #     database="mydb",
    #     user="postgres",
    #     password=""
    # )
    # connection.autocommit = True
    # cursor = connection.cursor()

    # combining the create table command into one string
    cursor = connection.cursor()


    # delete preexisting mydb if it conflicts with current mydb
    cursor.execute("DROP DATABASE IF EXISTS mydb")

    # Creating a database
    cursor.execute('CREATE database mydb;')

    # making user table within larer database
    cursor.execute('DROP TABLE IF EXISTS users;')
    create_table = '''
        CREATE TABLE users(
            id SERIAL NOT NULL,
            phone_number varchar(15) UNIQUE NOT NULL,
            email varchar(255) UNIQUE CHECK (POSITION('@' IN email) > 1),
            password varchar(255) NOT NULL,
            first_name varchar(255) NOT NULL,
            last_name varchar(255) NOT NULL,
            street varchar(255) NOT NULL,
            city varchar(255) NOT NULL,
            state varchar(2) NOT NULL,
            zip_code VARCHAR(5) NOT NULL,
            annual_income BIGINT NOT NULL,
            family_size SMALLINT NOT NULL,
            PRIMARY KEY(id)
        );
        CREATE TABLE IF NOT EXISTS items(
            item_id SERIAL PRIMARY KEY,
            item_url text,
            name VARCHAR(255) NOT NULL,
            price DECIMAL NOT NULL
        );
    '''

    # create user table
    cursor.execute(create_table)

    print("Database created successfully........")
    print("Tables created successfully..........")

    # Closing the connection
    cursor.close()
    connection.close()

setup()