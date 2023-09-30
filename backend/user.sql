CREATE TABLE user(
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