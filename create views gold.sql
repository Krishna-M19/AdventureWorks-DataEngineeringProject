
CREATE SCHEMA gold;

CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'xxxxxxxxx';




-----------------------------
--CREATE VIEW CALENDAR
-----------------------------
CREATE VIEW gold.calendar
AS
SELECT
    *
FROM
    OPENROWSET
     (
        BULK 'https://advdatastorage1.dfs.core.windows.net/silver-trans/AdventureWorks_Calendar/',
        FORMAT = 'PARQUET'
     ) as QUERY1

----------------------------------------
----CREATE VIEW CUSTOMER-----
---------------------------------
CREATE VIEW gold.customers
AS
SELECT
    *
FROM
    OPENROWSET
     (
        BULK 'https://advdatastorage1.dfs.core.windows.net/silver-trans/AdventureWorks_Customers/',
        FORMAT = 'PARQUET'
     ) as QUERY1

--------------------------------------
------CREATE VIEW PRODUCT CATEGORIES----
-------------------------------------
CREATE VIEW gold.product_categories
AS
SELECT
    *
FROM
    OPENROWSET
     (
        BULK 'https://advdatastorage1.dfs.core.windows.net/silver-trans/AdventureWorks_Product_Categories/',
        FORMAT = 'PARQUET'
     ) as QUERY1

-----------------------------------
----CREATE  VIEW PRODUCTS------
-------------------------------------
CREATE VIEW gold.products
AS
SELECT
    *
FROM
    OPENROWSET
     (
        BULK 'https://advdatastorage1.dfs.core.windows.net/silver-trans/AdventureWorks_Products/',
        FORMAT = 'PARQUET'
     ) as QUERY1


----------------------------------
----CREATE VIEW REUTUNS---------
-------------------------------
CREATE VIEW gold.retur
AS
SELECT
    *
FROM
    OPENROWSET
     (
        BULK 'https://advdatastorage1.dfs.core.windows.net/silver-trans/AdventureWorks_Returns/',
        FORMAT = 'PARQUET'
     ) as QUERY1

----------------------------------
----CREATE VIEW SALES---------
--------------------------------
CREATE VIEW gold.sales
AS
SELECT
    *
FROM
    OPENROWSET
     (
        BULK 'https://advdatastorage1.dfs.core.windows.net/silver-trans/AdventureWorks_sales/',
        FORMAT = 'PARQUET'
     ) as QUERY1



-------------------------------
----CREATE VIEW TERRITORIES----
-------------------------------
CREATE VIEW gold.territories
AS
SELECT
    *
FROM
    OPENROWSET
     (
        BULK 'https://advdatastorage1.dfs.core.windows.net/silver-trans/AdventureWorks_Territories/',
        FORMAT = 'PARQUET'
     ) as QUERY1