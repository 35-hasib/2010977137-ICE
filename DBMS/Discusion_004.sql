
-- 1
create trigger print_test on Item for insert
as
begin
	print 'Data is inserted into Item Table'
end

-- 2
create trigger trg_update_item on Transactions for insert
as 
begin
	declare @item_id verchar(6), @tranamnt int, @tran_type char(1)
	select @item_id=item_id, @tranamnt=tran_quantity
end



