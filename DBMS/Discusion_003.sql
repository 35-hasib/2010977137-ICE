
-- Task 01

CREATE PROC GetCategorySummary001
AS
BEGIN 
    SELECT item_category as [Category], SUM(item_qty) AS [Total Number of Items],AVG(item_price) AS [Average Price]
    FROM Item
    GROUP BY item_category;
END;
--drop proc GetCategorySummary001
exec GetCategorySummary001

-- Task 02

CREATE PROC GetItemsCheaperThan
    @CategoryName VARCHAR(50),
    @Price FLOAT
AS
BEGIN
    SELECT *
    FROM Item
    WHERE item_category = @CategoryName AND item_price < @Price;
END;
-- drop proc GetItemsCheaperThan
exec GetItemsCheaperThan @CategoryName = 'Software', @Price = 100


-- Task 03

CREATE PROCEDURE UpdatePricesToTarget
    @CategoryName VARCHAR(50),
    @DesiredAvgPrice FLOAT
AS
BEGIN
    DECLARE @CurrentAvgPrice FLOAT;

    -- Calculate the current average price for the category
    SELECT @CurrentAvgPrice = AVG(item_price)
    FROM Item
    WHERE item_category = @CategoryName;

    -- Loop until the current average price exceeds the desired value
    WHILE @CurrentAvgPrice <= @DesiredAvgPrice
    BEGIN
        -- Update the price of items under the category by 10%
        UPDATE Item
        SET item_price = item_price * 1.10
        WHERE item_category = @CategoryName;

        -- Recalculate the current average price
        SELECT @CurrentAvgPrice = AVG(item_price)
        FROM Item
        WHERE item_category = @CategoryName;
    END;
END;

EXEC UpdatePricesToTarget @CategoryName = 'Software', @DesiredAvgPrice = 120;

