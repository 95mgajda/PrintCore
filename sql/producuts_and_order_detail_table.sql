-- === PRODUCTS ===
CREATE TABLE dbo.Products (
    Product_ID INT IDENTITY(1,1) PRIMARY KEY,
    Product_Name VARCHAR(100) NOT NULL,
    Category VARCHAR(50),
    Price DECIMAL(10, 2) NOT NULL
);

-- === ORDER DETAILS ===
CREATE TABLE dbo.OrderDetails (
    OrderDetail_ID INT IDENTITY(1,1) PRIMARY KEY,
    Order_ID INT NOT NULL,
    Product_ID INT NOT NULL,
    Quantity INT NOT NULL,
    Total_Price DECIMAL(10, 2) NOT NULL,

    FOREIGN KEY (Order_ID) REFERENCES dbo.Orders(Order_ID),
    FOREIGN KEY (Product_ID) REFERENCES dbo.Products(Product_ID)
);
