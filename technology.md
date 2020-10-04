# Technologies Used

## Data Cleaning and Analysis
Python, and Pandas, and Numpy libraries will be used to clean, parse and investigate the data.

## Database Storage
The Data will be stored on an AWS platform and displayed with an RDS created through AWS and Padmin PostgreSQL. Spark will be used to create a session in order to utilize pySpark. The data will be read from AWS S3, and PGAdmin will be used to create a table that matches the columns in the database. The dataframe will then be copied into the RDS.

## Machine Learning
This model will be created with the intention of determining whether or not a Kickstarter campaign will be successful, so it will be a binary classification. SciKitLearn is the machine learning library that will be used to create a classifier.

## Dashboard 
The dashboard to display the data and findings will be based on a flask template.
