-- pos_tables.sql
CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10, 2)
);