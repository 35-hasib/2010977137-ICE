
--------------------------------------------------------------------
-- Store procedure
--------------------------------------------------------------------
go
alter proc insert_treasection
@Transaction_ID CHAR(4),
@Transaction_date DATE,
@Customer_ID CHAR(4),
@Product_ID CHAR(4),
@Quantity_sold INT
as
begin
	declare @Unit_Price money, @Quantity_in_hand int, @amount money;

	select @Unit_Price = Unit_Price, @Quantity_in_hand = Quantity_in_hand from Products
	where @Product_ID = Product_ID

	if @Quantity_sold <= @Quantity_in_hand
		begin
			set @amount = @Unit_Price * @Quantity_sold;
			print 'Total price = ' + cast(@amount as varchar(20))
		
			INSERT INTO Transactions (Transaction_ID, Transaction_date, Customer_ID, Product_ID, Quantity_sold)
			VALUES (@Transaction_ID, @Transaction_date, @Customer_ID, @Product_ID, @Quantity_sold);
		end
	else
	begin
		print 'Not enough stock !!'
	end
end
------------------------------------------------------------------------------------------
go
exec insert_treasection
	@Transaction_ID = 'T019',
    @Transaction_date = '2025-01-21',
    @Customer_ID = 'C002',
    @Product_ID = 'P001',
    @Quantity_sold = 10;

-------------------------------------------------------------------------------------------
-- Trigger
-------------------------------------------------------------------------------------------

go
alter trigger update_transection on Transactions after insert
as
begin
	select * from inserted
	declare @Transaction_ID varchar(4), @Customer_ID varchar(4), @Product_ID varchar(4), @Quantity_sold int;

	select @Transaction_ID=Transaction_ID, @Customer_ID=Customer_ID, @Product_ID=Product_ID, @Quantity_sold=Quantity_sold from inserted

	update Products
	set Quantity_in_hand = Quantity_in_hand - @Quantity_sold
	where Product_ID = @Product_ID

	declare @amount money, @Unit_Price int;
	select @Unit_Price =  Unit_Price from Products where Product_ID = @Product_ID

	update Customers
	set Total_sale_amount = Total_sale_amount + @Unit_Price * @Quantity_sold
	where Customer_ID=@Customer_ID

	print 'Data inserted !!'

end

---------------------------------------------------------------------------------------
-- If i delect a transection then 
---------------------------------------------------------------------------------------

go
alter trigger update_transection1 on Transactions after delete
as
begin
	print 'Delete one Transection !!'
	select * from deleted
end

select * from Transactions
delete from Transactions where Transaction_ID = 'T002'

