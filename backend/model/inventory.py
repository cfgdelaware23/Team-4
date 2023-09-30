from dbconnect import connection
class Item:
    item_schema = {
        "name": str,
        "price": float
    }

    @staticmethod
    def add_item(item):
        cursor = connection.cursor()
        query = """
                INSERT INTO items (
                    name, 
                    price
                ) VALUES ( 
                    %s, %s
                ) 
                ON CONFLICT (name) 
                DO UPDATE SET 
                    price = EXCLUDED.price
                RETURNING *;
                """
        cursor.execute(query, (
            item["name"],
            item["price"]
        ))
        updated_item = cursor.fetchone()
        connection.commit()
        cursor.close()
        return updated_item

    @staticmethod
    def get_item(item_id):
        cursor = connection.cursor()
        query = """
                SELECT * FROM items WHERE item_id = %s;
                """
        cursor.execute(query, (item_id,))
        item = cursor.fetchone()
        cursor.close()
        return item

    @staticmethod
    def get_all_items():
        cursor = connection.cursor()
        query = "SELECT * FROM items;"
        cursor.execute(query)
        items = cursor.fetchall()
        cursor.close()
        return items