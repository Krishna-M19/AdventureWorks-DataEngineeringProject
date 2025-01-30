# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

# MAGIC %md
# MAGIC ###SILVER LAYER SCRIPT###
# MAGIC ##Data Access Using APP Service##

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.advdatastorage1.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.advdatastorage1.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.advdatastorage1.dfs.core.windows.net", "application_ID xxxxxx_Xxxxxx_xxxxx")
spark.conf.set("fs.azure.account.oauth2.client.secret.advdatastorage1.dfs.core.windows.net", "secret_value XXXXX_xxxxxx_xxxxxx")
spark.conf.set("fs.azure.account.oauth2.client.endpoint.advdatastorage1.dfs.core.windows.net", "https://login.microsoftonline.com/directory_tenant xxxxx_xxxx_xxx/oauth2/token")

# COMMAND ----------

# MAGIC %md
# MAGIC #### Read/Load Data ###

# COMMAND ----------

df_cal = spark.read.format("csv")\
                    .option("header", True)\
                    .option("inferSchema", True)\
                    .load("abfss://bronze-raw@advdatastorage1.dfs.core.windows.net/AdventureWorks_Calendar/AdventureWorks_Calendar.csv")

# COMMAND ----------

df_cus = spark.read.format("csv")\
            .option("header", True)\
            .option("inferSchema", True)\
            .load("abfss://bronze-raw@advdatastorage1.dfs.core.windows.net/AdventureWorks_Customers/AdventureWorks_Customers.csv")

# COMMAND ----------

df_pcat = spark.read.format("csv")\
            .option("header", True)\
            .option("inferSchema", True)\
            .load("abfss://bronze-raw@advdatastorage1.dfs.core.windows.net/AdventureWorks_Product_Categories/AdventureWorks_Product_Categories.csv")

# COMMAND ----------

df_psub = spark.read.format("csv")\
            .option("header", True)\
            .option("inferSchema", True)\
            .load("abfss://bronze-raw@advdatastorage1.dfs.core.windows.net/AdventureWorks_Product_Subcategories/AdventureWorks_Product_Subcategories.csv")

# COMMAND ----------

df_prod = spark.read.format("csv")\
            .option("header", True)\
            .option("inferSchema", True)\
            .load("abfss://bronze-raw@advdatastorage1.dfs.core.windows.net/AdventureWorks_Products/AdventureWorks_Products.csv")

# COMMAND ----------

df_ret = spark.read.format("csv")\
            .option("header", True)\
            .option("inferSchema", True)\
            .load("abfss://bronze-raw@advdatastorage1.dfs.core.windows.net/AdventureWorks_Returns/AdventureWorks_Returns.csv")

# COMMAND ----------

df_s15 = spark.read.format("csv")\
            .option("header", True)\
            .option("inferSchema", True)\
            .load("abfss://bronze-raw@advdatastorage1.dfs.core.windows.net/AdventureWorks_Sales_2015/AdventureWorks_Sales_2015.csv")

# COMMAND ----------

df_s16 = spark.read.format("csv")\
            .option("header", True)\
            .option("inferSchema", True)\
            .load("abfss://bronze-raw@advdatastorage1.dfs.core.windows.net/AdventureWorks_Sales_2016/AdventureWorks_Sales_2016.csv")

# COMMAND ----------

df_s17 = spark.read.format("csv")\
            .option("header", True)\
            .option("inferSchema", True)\
            .load("abfss://bronze-raw@advdatastorage1.dfs.core.windows.net/AdventureWorks_Sales_2017/AdventureWorks_Sales_2017.csv")

# COMMAND ----------

df_ter = spark.read.format("csv")\
            .option("header", True)\
            .option("inferSchema", True)\
            .load("abfss://bronze-raw@advdatastorage1.dfs.core.windows.net/AdventureWorks_Territories/AdventureWorks_Territories.csv")

# COMMAND ----------

df_sales= spark.read.format("csv")\
            .option("header", True)\
            .option("inferSchema", True)\
            .load("abfss://bronze-raw@advdatastorage1.dfs.core.windows.net/AdventureWorks_Sales*")

# COMMAND ----------

# MAGIC %md
# MAGIC #### TRANSFORMATIONS####

# COMMAND ----------

df_cal= df_cal.withColumn("Month", month(col("Date")))\
                .withColumn("Year", year(col("Date")))
df_cal.display()

# COMMAND ----------

df_cal.write.format('parquet')\
        .mode('append')\
        .option("path" , "abfss://silver-trans@advdatastorage1.dfs.core.windows.net/AdventureWorks_Calendar")\
        .save()

# COMMAND ----------

## Customer Data Transformation

df_cus.display()

# COMMAND ----------

df_cus.withColumn("FullName", concat(col("Prefix"), lit(" "), col("FirstName"), lit(" "), col("LastName"))).display()

# COMMAND ----------

df_cus= df_cus.withColumn("FullName", concat_ws(" ", col("Prefix"), col("FirstName"), col("LastName")))
df_cus.display()

# COMMAND ----------

df_cus.write.format('parquet')\
        .mode('append')\
        .option("path" , "abfss://silver-trans@advdatastorage1.dfs.core.windows.net/AdventureWorks_Customers")\
        .save()

# COMMAND ----------

### Product Category Data Transformation
df_pcat.display()

# COMMAND ----------

df_pcat.write.format('parquet')\
        .mode('append')\
        .option("path" , "abfss://silver-trans@advdatastorage1.dfs.core.windows.net/AdventureWorks_Product_Categories")\
        .save()

# COMMAND ----------

df_prod.display()

# COMMAND ----------

df_prod= df_prod.withColumn("ProductSKU", split(col("ProductSKU"), "-")[0])\
                 .withColumn("ProductName", split(col("ProductName"), " ")[0])

# COMMAND ----------

df_prod.display()

# COMMAND ----------

df_prod.write.format('parquet')\
        .mode('append')\
        .option("path" , "abfss://silver-trans@advdatastorage1.dfs.core.windows.net/AdventureWorks_Products")\
        .save()

# COMMAND ----------

df_ret.display()

# COMMAND ----------

df_ret.write.format('parquet')\
        .mode('append')\
        .option("path" , "abfss://silver-trans@advdatastorage1.dfs.core.windows.net/AdventureWorks_Returns")\
        .save()

# COMMAND ----------

df_ter.display()

# COMMAND ----------

df_ter.write.format('parquet')\
        .mode('append')\
        .option("path" , "abfss://silver-trans@advdatastorage1.dfs.core.windows.net/AdventureWorks_Territories")\
        .save()

# COMMAND ----------

df_sales.display()

# COMMAND ----------

df_sales = df_sales.withColumn("StockDate", to_timestamp('StockDate'))\
                     .withColumn("OrderNumber", regexp_replace(col('OrderNumber'), 'S', 'T'))\
                     .withColumn("Multiply", col("OrderLineItem")*col("OrderQuantity"))

# COMMAND ----------

df_sales.display()

# COMMAND ----------

df_sales.write.format('parquet')\
        .mode('append')\
        .option("path" , "abfss://silver-trans@advdatastorage1.dfs.core.windows.net/AdventureWorks_Sales")\
        .save()

# COMMAND ----------

# MAGIC %md
# MAGIC ###Sales Analysis###

# COMMAND ----------

df_sales.groupBy("OrderDate").agg(count("OrderNumber").alias("TotalOrders")).display()

# COMMAND ----------

df_pcat.display()

# COMMAND ----------

df_ter.display()

# COMMAND ----------

