# AdventureWorks-DataEngineeringProject
Real-time Data Engineering Project on Azure
This project demonstrates a real-time data engineering pipeline implemented on Azure. The goal is to ingest, transform, and serve data using Azure's suite of services, including Azure Data Lake, Azure Data Factory (ADF), Azure Databricks, and Azure Synapse Analytics. The pipeline is based on the Medallion Architecture, consisting of three layers: Bronze, Silver, and Gold.

Project Overview
The project is structured in three main phases:

Phase 1: Data Ingestion and Raw Data Storage
Phase 2: Data Transformation Using Azure Databricks
Phase 3: Data Serving and Access with Azure Synapse Analytics
Additionally, the project integrates with Power BI for data visualization and reporting.

Phase 1: Data Ingestion and Raw Data Storage
Objective: Ingest data from external sources and store it in Azure Data Lake using Azure Data Factory (ADF) as the ETL tool. This data is organized in the Bronze Layer of the Medallion Architecture, representing raw, unprocessed data.

Steps Involved:
Resource Group and Data Lake Setup:

Created an Azure Resource Group named Adventure Project to organize all related Azure resources.
Set up an Azure Data Lake Storage Gen2 account for scalable and efficient storage.
Created three containers within the Data Lake for each layer of the Medallion Architecture:
Bronze: For raw, unprocessed data.
Silver: For cleansed and transformed data.
Gold: For refined, aggregated data ready for analytics.
Azure Data Factory Setup:

Created an Azure Data Factory (ADF) instance to orchestrate the data ingestion pipeline.
Set up an HTTP Linked Service to connect ADF to external data sources (in this case, the GitHub API).
Created an Azure Data Lake Storage Gen2 Linked Service to connect ADF to the Data Lake.
Dynamic Pipeline Creation in ADF:

Developed a parameterized dynamic pipeline called "DynamicGitToRaW" for data ingestion.
Used ForEach Activity to process multiple datasets, dynamically passing parameters such as:
HTTP URLs for API requests
Locations for storing CSV files
Output folder paths in the Data Lake.
Created a LookUp Activity to pull dynamic parameters from a JSON file stored in Data Lake, making the pipeline flexible and reusable.
Data Ingestion to the Bronze Layer:

Ingested raw data from the GitHub API into the bronze layer in CSV format.
This raw data is now available in the Data Lake for transformation in later phases.
Phase 2: Data Transformation Using Azure Databricks
Objective: Perform data transformation and cleansing using Azure Databricks with Apache Spark to process the raw data from the Bronze Layer and store the results in the Silver Layer.

Steps Involved:
Azure Databricks Setup:

Created an Azure Databricks resource for data processing.
Configured a Spark Cluster with the following specifications:
1 Node, 14 GB of Memory, 4 Cores.
Apache Spark 3.5.0 and Scala 2.12 for running transformation jobs.
Accessing Data from Data Lake:

Configured Azure Service Principal and used Access Control (IAM) in Azure Data Lake to allow Databricks to read data from the bronze layer.
Generated certificates and secrets for authentication between Databricks and the Data Lake.
Data Transformation with PySpark:

Accessed raw data in the bronze layer using PySpark and Spark DataFrames.
Applied several data transformations, including:
Date Parsing: Extracting year and month from calendar data.
Concatenation: Combining first name, last name, and prefix to create a full name.
Data Cleansing: Processing product SKUs and names.
Transformed data for different tables (e.g., Sales, Products, Customers) and stored the results in Parquet format in the silver layer.
Data Storage in the Silver Layer:

The transformed data is now available in the silver layer of the Data Lake, cleaned and enriched for analytics.
Phase 3: Data Serving and Access with Azure Synapse Analytics
Objective: Use Azure Synapse Analytics to create a serving layer that connects to both the silver and gold containers in the Data Lake, structuring the data for analytics and reporting.

Steps Involved:
Azure Synapse Analytics Setup:

Created an Azure Synapse Analytics resource to act as the serving layer.
Configured SQL Pools (both dedicated and serverless) for querying data and Spark Pools for data processing.
Used Synapse’s Data Integration and Develop options for orchestrating pipelines and running Spark-based transformations.
Permissions and Security Setup:

Utilized System Managed Identity for Synapse to securely access both the silver and gold containers in the Data Lake.
Created role assignments within Data Lake’s IAM settings to enable seamless data access.
Serverless SQL Pool and Data Abstraction:

Employed serverless SQL Pools in Synapse to query data directly in the Data Lake without moving the data.
Implemented a data lakehouse architecture, where the data remains in the Data Lake and an abstraction layer (metadata layer) is created in Synapse for efficient querying.
Creating External Tables and Views:

Created external tables and views in the gold schema using OPENROWSET to query data stored in the silver layer of the Data Lake.
Used CETAS (Create External Table As Select) to push data from the silver container into the gold container, optimizing the data for reporting.
Stored the data in Parquet format with Gzip compression for better query performance and reduced storage size.
Metadata and Querying:

Stored metadata in external views to allow efficient querying without duplicating data.
Queried the data from the gold schema for reporting and analysis purposes.
