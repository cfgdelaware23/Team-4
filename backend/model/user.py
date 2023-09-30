from dbconnect import connection
class User:
    user_schema = {
        "first_name": str,
        "last_name": str,
        "phone_number": str,
        "email": str,
        "password": str,
        "confirm_password": str,
        "address": {
            "street": str,
            "city": str,
            "state": str,
            "zip_code": int,
        },
        "annual_income": int,
        "family_size": int,
    }

    @staticmethod
    def register(user):
        print(user)
        cursor = connection.cursor()
        query = """
                    INSERT INTO users (
                        first_name, 
                    ["last_name,
"]                        phone_number,
                        email,
                        password,              
                        confirmPassword,
                        street,
                        city,
                        state,
                        zipCode,
                        waysOfCommute,
                        familySize,
                    ) VALUES ( 
                        %s %s %s %s %s %s %s %s %s %i
                    )
                """
        cursor.execute(query, (
            user["firstName"],
            user["lastName"],
            user["phoneNum"],
            user["email"],
            user["password"],
            user["street"],
            user["city"],
            user["state"],
            user["zipCode"],
            user["familySize"],
        ))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def login( user):
        pass


User.register({
    "firstName": "Jane",
    "lastName": "Doe",
    "phoneNum": "1234567890",
    "email": "janedoe@test.com",
    "password": "",
    "confirmPassword": "",
    "street": "Hicks Way",
    "city": "Amherst",
    "state": "MA",
    "zipCode": "01003",
    "familySize": 0
})


    