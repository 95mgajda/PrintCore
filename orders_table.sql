create table dbo.Orders (
	Order_ID int identity(1,1) primary key,
	Client_ID int not null,
	Order_Date Datetime not null default getdate(),
	Order_Amount decimal(10, 2) not null,
	FOREIGN key (Client_ID) references dbo.Clients_Test(Client_ID)
);