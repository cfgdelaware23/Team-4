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
    def register(self, user):
        pass

    @staticmethod
    def login(self, user):
        pass

    

    