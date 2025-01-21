
-- 1
create trigger print_test on Item for insert
as
begin
	print 'Data is inserted into Item Table'
end

-- 2
create trigger trg_update_item on Transactions



