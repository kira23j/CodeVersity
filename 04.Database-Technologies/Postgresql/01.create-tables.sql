-- Create the customer table
CREATE TABLE customer (
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(60) NOT NULL,
    company VARCHAR(60) NOT NULL,
    street VARCHAR(60) NOT NULL,
    city VARCHAR(30) NOT NULL,
    state CHAR(30) NOT NULL,
    zip SMALLINT NOT NULL,
    phone VARCHAR(20) NOT NULL,
    birthday DATE NULL,
    sex CHAR(1) NOT NULL,
    date_entered TIMESTAMP NOT NULL,
    id SERIAL PRIMARY KEY,
);

-- Insert a sample record into the customer table
INSERT INTO customer (first_name, last_name, email, company, street, city, state, zip, phone, birthday, sex, date_entered)
VALUES  ('John', 'Doe', 'johndoe@gmail.com', 'Acme Inc.', '123 Main St', 'Anytown', 'CA', 12345, '555-1234', '1980-01-01', 'M', CURRENT_TIMESTAMP);

-- Create the enum type for sex
CREATE TYPE  sex_type AS ENUM ('M', 'F');

-- Alter the table to use the new enum
ALTER table customer
    ALTER COLUMN sex TYPE sex_type
    USING sex::sex_type;

-- Create the sales_person table
CREATE TABLE sales_person(
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(60) NOT NULL,
    company VARCHAR(60) NOT NULL,
    street VARCHAR(60) NOT NULL,
    city VARCHAR(30) NOT NULL,
    state CHAR(30) NOT NULL,
    zip SMALLINT NOT NULL,
    phone VARCHAR(20) NOT NULL,
    birthday DATE NULL,
    sex sex_type NOT NULL,
    date_hired TIMESTAMP NOT NULL,
    id SERIAL PRIMARY KEY
);


CREATE TABLE product_type (
    name VARCHAR(30) NOT NULL,
    id SERIAL PRIMARY KEY
);


CREATE TABLE product(
type_id INT REFERENCES product_type(id),
name VARCHAR(30) NOT NULL,
supplier VARCHAR(30) NOT NULL,
description TEXT NOT NULL,  
id SERIAL PRIMARY KEY
);

-- Insert a sample record into the product_type table
CREATE TABLE item  (
    product_id INT REFERENCES product(id),
    size INT NOT NULL,
    color VARCHAR(30) NOT NULL,
    picture VARCHAR(256) NOT NULL,
    price NUMERIC(6, 2) NOT NULL,
    ID SERIAL PRIMARY KEY
);

-- 
CREATE TABLE sales_order(
    cust_id INT REFERENCES customer(id),
    sales_person_id INT REFERENCES sales_person(id),
    item_order_taken TIMESTAMP NOT NULL,
    purchase_order_number INT NOT NULL,
    credit_card_number VARCHAR(20) NOT NULL,
    creadit_card_exper_month SMALLINT NOT NULL,
    credit_card_exper_day SMALLINT NOT NULL,
    credit_card_exper_year SMALLINT NOT NULL,
    id SERIAL PRIMARY KEY
);

-- 
CREATE TABLE sales_item (
    item_id INT REFERENCES item(id),
    sales_order_id INT REFERENCES sales_order(id),
    quantity INT NOT NULL,
    discount NUMERIC(4, 2) NOT NULL,
    taxable BOOLEAN NOT NULL,
    sales_tax_rate NUMERIC(5, 2) NOT NULL DEFAULT 0,
    id SERIAL PRIMARY KEY
); 