# AdventureWorks Real-time Data Engineering Project on Azure Data Engineering

## Phase 1: Data Ingestion and Raw Data Storage

### Objective:
- Ingest data from external sources and store it in the Azure Data Lake using Azure Data Factory (ADF) as the ETL tool.
- Organize the data in the bronze layer of the Medallion Architecture.

### Steps Involved:

#### Resource Group and Data Lake Setup:
- Created an Azure resource group named "Adventure Project" to house all Azure resources related to the project.
- Set up an Azure Data Lake Storage Gen2 for efficient, scalable data storage. Created separate containers within the Data Lake for bronze, silver, and gold layers.

#### Azure Data Factory Setup:
- Created an Azure Data Factory (ADF) instance for orchestrating data ingestion pipelines.
- Built an **HTTP Linked Service** to connect ADF to external data sources (in this case, GitHub API's).
- Created an **Azure Data Lake Storage Gen2 Linked Service** for connecting ADF to the Data Lake.

#### Dynamic Pipeline Creation in ADF:
- Developed a parameterized dynamic pipeline named **"DynamicGitToRaW"** in ADF for ingesting data.
- Used **ForEach Activity** to loop over and process multiple datasets, passing dynamic parameters for HTTP URLs, CSV file locations, and output folder paths in the Data Lake.
- Created a **LookUp Activity** to pull data from a JSON file stored in Data Lake to provide parameters for the pipeline.

#### Data Ingestion to Bronze Layer:
- Ingested raw data from the GitHub API into the bronze layer of the Azure Data Lake in CSV format. This data was stored as raw, unprocessed data, ready for transformation in later phases.

---

## Phase 2: Data Transformation Using Azure Databricks

### Objective:
- Perform data transformation and cleansing using Azure Databricks with Apache Spark to process the raw data from the bronze layer and store the results in the silver layer.

### Steps Involved:

#### Azure Databricks Setup:
- Created an Azure Databricks resource within the existing resource group for data processing.
- Configured a **Spark Cluster** with 1 node (14 GB memory, 4 cores) using **Apache Spark 3.5.0** and **Scala 2.12** for running data transformation jobs.

#### Accessing Data from Data Lake:
- Configured **Azure Service Principal** and used **Access Control (IAM)** in Azure Data Lake to allow Databricks to read from the bronze layer of the Data Lake.
- Generated certificates and secrets to authenticate the Databricks cluster with the Data Lake.

#### Data Transformation with PySpark:
- Accessed the raw data stored in the bronze layer using **PySpark** and **Spark DataFrames**.
- Applied various data transformations, such as:
  - **Date Parsing**: Extracting year and month from calendar data.
  - **Concatenation**: Creating a `FullName` column for customer data by combining first, last, and prefix names.
  - **Data Cleansing**: Splitting and processing product SKU and names for the product data.
- Transformed data for each table (e.g., **Sales**, **Products**, **Customers**) and wrote the results in **Parquet format** into the silver layer of the Data Lake.

#### Data Storage in Silver Layer:
- Transformed data was stored in the **silver container** of the Data Lake, ensuring that the data was cleaned and enriched for further use in analytics.

---

## Phase 3: Data Serving and Access with Azure Synapse Analytics

### Objective:
- Leverage Azure Synapse Analytics for creating a serving layer that connects to both the silver and gold containers in Data Lake, where data will be structured for analytics and reporting.

### Steps Involved:

#### Azure Synapse Analytics Setup:
- Created an Azure Synapse Analytics resource to act as the serving layer, enabling data querying and analysis.
- Configured **SQL Pools** (both **dedicated** and **serverless**) for querying data.
- Created a **Spark Pool** within Synapse for data processing and transformation tasks.
- Utilized the **Data Integration** and **Develop** options in Synapse for orchestrating pipelines and running Spark code.

#### Permissions and Security Setup:
- Used **System Managed Identity** to set up permissions for Synapse to access both silver and gold containers in the Data Lake.
- Created role assignments and Managed Identity within the Data Lake’s IAM settings to ensure secure access between Synapse and the Data Lake.

#### Serverless SQL Pool and Data Abstraction:
- Employed **serverless SQL Pools** in Synapse to access data stored in Data Lake without physically moving the data.
- Implemented a **data lakehouse** architecture by creating an abstraction layer where the data in the silver container could be accessed through views in the gold schema in Synapse.

#### Creating External Tables and Views:
- Created external tables and views in the **gold schema** using **OPENROWSET** to directly query data stored in the silver layer of the Data Lake.
- Created a **parquet file format** with **gzip compression** to improve query performance and reduce storage requirements.
- Used **CETAS** (Create External Table As Select) to push data from the silver container to the gold container for optimized querying.

#### Metadata and Querying:
- Stored metadata about the data in external views, enabling efficient querying and access without duplicating the data.
- Query results were stored in the **gold container**, ensuring that refined data could be used for reporting and further analysis.

#### Database Encryption and Credentials:
- Configured **master keys** for database encryption to ensure secure handling of sensitive data.
- Created external data sources and external file formats to manage the connection between Synapse SQL Pools and the Data Lake.

#### External Table Creation and Data Access:
- Created external tables such as **extsales** to represent refined data for consumption by BI tools.
- Enabled query access to external tables for fast and efficient analytics in Synapse.

---

## Final Integration with BI Tools (Power BI)

### Objective:
- Integrate the gold layer of data with Power BI for data visualization and reporting.

#### Connecting Power BI to Synapse Analytics:
- Configured **Power BI** to connect directly to the **Synapse Analytics views** and external tables in the **gold schema** for visualization and reporting.
- Utilized **DirectQuery** mode to query Synapse SQL Pools in real-time for up-to-date reporting.

---

### Summary:
This project effectively demonstrates a full **Real-time Data Engineering** pipeline using **Azure Data Engineering** tools. By combining **Azure Data Factory**, **Azure Databricks**, and **Azure Synapse Analytics**, the project efficiently processes raw data, transforms it, and makes it available for reporting and analysis via **Power BI**. The solution follows the **Medallion Architecture** (Bronze, Silver, Gold layers) for optimized data storage and processing, making it scalable and secure for large-scale analytics.
