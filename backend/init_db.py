from dbconnect import connection

def setup():
    # create a cursor to execute sql database commands
    cursor = connection.cursor()


    # delete preexisting mydb if it conflicts with current mydb
    cursor.execute('''DROP DATABASE IF EXISTS mydb''')

    # Creating a database
    cursor.execute('CREATE database mydb;')

    # making user table within larer database
    cursor.execute('DROP TABLE IF EXISTS users;')

    # combining the create table command into one string
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
    '''

    # create user table
    cursor.execute(create_table)

    print("Database created successfully........")
    print("User table created")

    # Closing the connection
    connection.close()

setup()
