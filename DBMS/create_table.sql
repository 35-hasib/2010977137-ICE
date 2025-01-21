

-- Creating table
CREATE TABLE CustomerAndSuppliers (
    cust_id CHAR(6) PRIMARY KEY CHECK (cust_id LIKE '[CS][0-9][0-9][0-9][0-9][0-9]'),
    cust_fname varCHAR(15) NOT NULL,
    cust_lname VARCHAR(15),
    cust_address TEXT,
    cust_telno CHAR(12) CHECK (cust_telno LIKE '[0-9][0-9][0-9][-][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
    cust_city CHAR(12) DEFAULT 'Rajshahi',
    sales_amnt MONEY CHECK (sales_amnt >= 0),
    proc_amnt MONEY CHECK (proc_amnt >= 0)
);
--drop table CustomerAndSuppliers
-- Insert random values into CustomerAndSuppliers table
INSERT INTO CustomerAndSuppliers (cust_id, cust_fname, cust_lname, cust_address, cust_telno, sales_amnt, proc_amnt)
VALUES 
    ('C00001', 'John', 'Doe', '123 Main St', '012-34567890', 10000.50, 5000.25);

-- Verify the data
SELECT * FROM CustomerAndSuppliers;


-- Creating the Item table
CREATE TABLE Item (
    item_id CHAR(6) PRIMARY KEY CHECK (item_id LIKE 'P[0-9][0-9][0-9][0-9][0-9]'),
    item_name CHAR(12),
    item_category CHAR(10) CHECK (item_category IN ('Electrical', 'Mechanical', 'Software', 'Books')),
    item_price FLOAT CHECK (item_price >= 0),
    item_qty INT CHECK (item_qty >= 0),
    item_last_sold DATE DEFAULT GETDATE()
);
--drop table Item
insert into Item 
values
('P00001', 'watch', 'Electrical', 66.0, 5,'2025-01-01'),
('P00002', 'windows', 'Software', 61.8, 4, '2025-02-02');

select * from Item

-- Creating the Transactions table
CREATE TABLE Transactions (
    tran_id CHAR(10) PRIMARY KEY CHECK (tran_id LIKE 'T[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
    item_id CHAR(6) NOT NULL,
    cust_id CHAR(6) NOT NULL,
    tran_type CHAR(1) CHECK (tran_type IN ('S', 'O')),
    tran_quantity INT NOT NULL CHECK (tran_quantity > 0),
    tran_date DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (item_id) REFERENCES Item(item_id),
    FOREIGN KEY (cust_id) REFERENCES CustomerAndSuppliers(cust_id)
);
--drop table Transactions

INSERT INTO Transactions (tran_id, item_id, cust_id, tran_type, tran_quantity, tran_date) VALUES
('T000000001', 'P00001', 'C00001', 'S', 20, '2025-01-18');


select * from CustomerAndSuppliers
select * from Item
select * from Transactions