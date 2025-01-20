

-- Creating table
CREATE TABLE CustomerAndSuppliers (
    cust_id varCHAR(6) PRIMARY KEY CHECK (cust_id LIKE '[CS][0-9][0-9][0-9][0-9][0-9]'),
    cust_fname varCHAR(15) NOT NULL,
    cust_lname VARCHAR(15),
    cust_address TEXT,
    cust_telno CHAR(12) CHECK (cust_telno LIKE '[0-9][0-9][0-9][-][0-9][0-9[0-9][0-9][0-9][0-9][0-9][0-9]'),
    cust_city CHAR(12) DEFAULT 'Rajshahi',
    sales_amnt MONEY CHECK (sales_amnt >= 0),
    proc_amnt MONEY CHECK (proc_amnt >= 0)
);


-- Creating the Item table
CREATE TABLE Item (
    item_id CHAR(6) PRIMARY KEY CHECK (item_id LIKE 'P[0-9][0-9][0-9][0-9][0-9]'),
    item_name CHAR(12),
    item_category CHAR(10) CHECK (item_category IN ('Electrical', 'Mechanical', 'Software', 'Books')),
    item_price FLOAT CHECK (item_price >= 0),
    item_qty INT CHECK (item_qty >= 0),
    item_last_sold DATE DEFAULT GETDATE()
);

-- Creating the Transactions table
CREATE TABLE Transactions (
    tran_id CHAR(10) PRIMARY KEY CHECK (tran_id LIKE 'T[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
    item_id CHAR(6) FOREIGN KEY REFERENCES Item(item_id),
    cust_id CHAR(6), -- Assuming there's a Customer table; reference can be added if needed
    tran_type CHAR(1) CHECK (tran_type IN ('S', 'O')),
    tran_quantity INT CHECK (tran_quantity > 0),
    tran_date DATETIME DEFAULT GETDATE()
);

select * from CustomerAndSuppliers
select * from Item
select * from Transactions