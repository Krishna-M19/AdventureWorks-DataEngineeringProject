CREATE DATABASE SCOPED CREDENTIAL cred_adventure
WITH IDENTITY = 'Managed Identity'

CREATE EXTERNAL DATA SOURCE source_silver
WITH
(
    LOCATION = 'https://advdatastorage1.dfs.core.windows.net/silver-trans',
    CREDENTIAL = cred_adventure
)
CREATE EXTERNAL DATA SOURCE source_gold
WITH
(
    LOCATION = 'https://advdatastorage1.dfs.core.windows.net/gold-serving',
    CREDENTIAL = cred_adventure
)


CREATE EXTERNAL FILE FORMAT parquet_format
WITH
(
    FORMAT_TYPE = PARQUET,
    DATA_COMPRESSION = 'org.apache.hadoop.io.compress.GzipCodec'
)


----------------------------------------
---- CREATE EXTERNAL TABLE EXTSALES------
------------------------------------------

CREATE EXTERNAL TABLE gold.extsales
WITH
(
    LOCATION = 'extsales',
    DATA_SOURCE = source_gold,
    FILE_FORMAT = parquet_format
)
AS
SELECT * FROM gold.sales 




SELECT* FROM gold.extsales
