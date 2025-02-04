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



--CREATE PROCEDURE sp_addTransaction
--    @Transaction_ID CHAR(4),
--    @Transaction_date DATE,
--    @Customer_ID CHAR(4),
--    @Product_ID CHAR(4),
--    @Quantity_sold INT,
--    @Amount MONEY OUTPUT
--AS
--BEGIN
--    DECLARE @Unit_Price MONEY;
--    DECLARE @Quantity_in_hand INT;
    
--    SELECT @Unit_Price = Unit_Price, @Quantity_in_hand = Quantity_in_hand FROM Products
--    WHERE Product_ID = @Product_ID;
    
--    IF @Quantity_sold <= @Quantity_in_hand
--    BEGIN
--        SET @Amount = @Unit_Price * @Quantity_sold;
        
--        INSERT INTO Transactions (Transaction_ID, Transaction_date, Customer_ID, Product_ID, Quantity_sold)
--        VALUES (@Transaction_ID, @Transaction_date, @Customer_ID, @Product_ID, @Quantity_sold);
        
--        UPDATE Products
--        SET Quantity_in_hand = Quantity_in_hand - @Quantity_sold
--        WHERE Product_ID = @Product_ID;
--    END
--
--END;

--DECLARE @Amount MONEY;
--EXEC sp_addTransaction @Transaction_ID = 'T002', 
--	@Transaction_date = '2025-01-21', 
--	@Customer_ID = 'C002', 
--	@Product_ID = 'P002', 
--	@Quantity_sold = 5, 
--	@Amount = @Amount OUTPUT; 

--CREATE TRIGGER trg_updateTables
--ON Transactions
--AFTER INSERT
--AS
--BEGIN
--    DECLARE @Customer_ID CHAR(4);
--    DECLARE @Product_ID CHAR(4);
--    DECLARE @Quantity_sold INT;
--    DECLARE @Amount MONEY;

--    SELECT @Customer_ID = inserted.Customer_ID, @Product_ID = inserted.Product_ID, @Quantity_sold = inserted.Quantity_sold
--    FROM inserted;
    
--    SELECT @Amount = Unit_Price * @Quantity_sold
--    FROM Products
--    WHERE Product_ID = @Product_ID;
    
--    UPDATE Customers
--    SET Total_sale_amount = Total_sale_amount + @Amount
--    WHERE Customer_ID = @Customer_ID;
--END;
--GO
