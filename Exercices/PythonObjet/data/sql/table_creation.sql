CREATE TABLE car (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(255),
    year INT,
    selling_price VARCHAR(100),--to easily convert to int
    present_price VARCHAR(100),--to easily convert to int
    km_driven VARCHAR(100),
    fuel VARCHAR(50),
    seller_type VARCHAR(50),
    transmission VARCHAR(50),
    owner VARCHAR(50)
);