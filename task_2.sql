-- Use the alx_book_store database
USE alx_book_store;

-- Create the 'books' table
-- This table stores information about books
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(130),
    author_id INT,
    price DOUBLE NOT NULL,
    publication_date DATE
);

-- Create the 'authors' table
-- This table stores information about the authors
CREATE TABLE authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(215)
);

-- Create the 'customers' table
-- This table stores information about the customers
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
);

-- Create the 'orders' table
-- This table stores information about customer orders
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE
);

-- Create the 'order_details' table
-- This table stores the details of each order
CREATE TABLE order_details (
    order_detail_id INT PRIMARY KEY,
    order_id INT,
    book_id INT,
    quantity DOUBLE
);