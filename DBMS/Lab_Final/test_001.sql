--create database shop
use shop
--CREATE DATABASE Shop; 
--USE Shop; 


CREATE TABLE Products (
    Product_ID CHAR(4) PRIMARY KEY CHECK (Product_ID LIKE 'P[0-9][0-9][0-9]'),
    Product_Name VARCHAR(100),
    Unit_Price MONEY,
    Quantity_in_hand INT
);

INSERT INTO Products VALUES 
('P001', 'ProductA', 20.00, 100), 
('P002', 'ProductB', 30.00, 200);


CREATE TABLE Customers (
    Customer_ID CHAR(4) PRIMARY KEY CHECK (Customer_ID LIKE 'C[0-9][0-9][0-9]'),
    First_Name VARCHAR(50),
    Last_Name VARCHAR(50),
    City VARCHAR(50),
    Total_sale_amount MONEY
);

INSERT INTO Customers VALUES 
('C001', 'John', 'Doe', 'CityA', 0.00), 
('C002', 'Jane', 'Smith', 'CityB', 0.00);


CREATE TABLE Transactions (
    Transaction_ID CHAR(4) PRIMARY KEY CHECK (Transaction_ID LIKE 'T[0-9][0-9][0-9]'),
    Transaction_date DATE,
    Customer_ID CHAR(4) FOREIGN KEY REFERENCES Customers(Customer_ID),
    Product_ID CHAR(4) FOREIGN KEY REFERENCES Products(Product_ID),
    Quantity_sold INT
);


INSERT INTO Transactions VALUES 
('T001', '2025-01-21', 'C001', 'P001', 10);


select * from Products
select * from Customers
select * from Transactions



