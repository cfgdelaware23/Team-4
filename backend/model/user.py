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
                    last_name,
                    phone_number,
                    email,
                    password,
                    street,
                    city,
                    state,
                    zip_code,
                    annual_income,
                    family_size
                ) VALUES ( 
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
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
            user["annualIncome"],
            user["familySize"],
        ))
        new_user = cursor.fetchone()
        connection.commit()
        cursor.close()
        connection.close()
        return new_user

    @staticmethod
    def login( user):
        pass


# User.register({
#     "firstName": "Jane",
#     "lastName": "Doe",
#     "phoneNum": "1334567890",
#     "email": "janedoe@tst.com",
#     "password": "",
#     "confirmPassword": "",
#     "street": "Hicks Way",
#     "city": "Amherst",
#     "state": "MA",
#     "zipCode": "01003",
#     "annualIncome": 1_000_000,
#     "familySize": 0
# })


    