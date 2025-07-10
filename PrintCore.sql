--ALTER PROCEDURE AddClient
--    @Client_ID INT,
--    @First_Name VARCHAR(50),
--    @Last_Name VARCHAR(50),
--    @Email VARCHAR(50),
--    @Phone VARCHAR(20),
--    @NIP VARCHAR(10),
--    @Client_Type VARCHAR(50)
--AS
--BEGIN
--    INSERT INTO Clients (Client_ID, First_Name, Last_Name, Email, Phone, NIP, Client_Type)
--    VALUES (@Client_ID, @First_Name, @Last_Name, @Email, @Phone, @NIP, @Client_Type);
--END;

--EXEC AddClient
--    @Client_ID = 11,
--    @First_Name = 'Magda',
--    @Last_Name = 'Zieliñska',
--    @Email = 'magda.zielinska@example.com',
--    @Phone = '888777666',
--    @NIP = '6677889900',
--    @Client_Type = 'B2B';

select * from orders;