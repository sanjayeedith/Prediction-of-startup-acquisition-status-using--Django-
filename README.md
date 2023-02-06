# Prediction-of-startup-acquisition-status 
The Prediction of Startup Acquisition Status is a process of determining the likelihood that a startup company will be acquired by another company. This prediction can be based on various factors such as the startup's financial performance, its market position, the state of the economy, and the acquisition history of similar companies. The objective of this prediction is to help investors, stakeholders, and entrepreneurs make informed decisions about investing in or acquiring startups.

The dataset is all about the Startup's Financial Information and we need to predict the current financial status of the company. The database is Crunchbase-2013, database, company, investors and all the other details belong to the company. In this project, we analyzed the company's status i.e, Operating, Acquired, IPO, or closed.

# Understand the Dataset

- Dataset Link: ( https://drive.google.com/file/d/17bfNyMgP-PofCkdlvnLHxxFqV8mdDo-9/view )
* The dataset is completely based ont the company's information from company's website of 2013.
+ Features: All the columns with the company's information like name, permalink, category, funding dates, funding rounds, funding amounts, city, state, last milestone dates many more.
- Target variable: Status

# Data Cleaning
+ We deleted with redundancy, granularity, and irrelevant information we also deleted instances with missing values for specific columns we removed NULL values for the following columns status, country_code, and Founded_at. The imputing method uses mean, median, and mode for the columns with less percentage of NULL values.


# Data Transformation
* Here we are fixing irrelevant data types to some columns so we converted columns to the included data year datatype.

- Then we started filling the NULL values in closed_at for calculation of the age of the company then we created column active_days from substrating colsed_at fro, founded _at then we removed rows with negative values in active_days and dropped the other two columns.

+ Then we removed outliers using the IQR method then we generalized category_code and country_code using One hot encoder to prepare for feature engineering by working on our targeted variable Status and we finalized the data analysis part by deleting duplicates from datasets.


# Model Building

* We started the ML part by applying the Logistic Regression Model, XGBoost Classifier Model, Quadratic Analysis Model, and Random Forest Classifier Model. But first, we had to prepare the data through the following steps.

a. Splitting the data. We split the data through SKlearn using test_train_split function.

b. Seprating numerical and categorical columns.

c. Applying one-hot encoding to the whole columns.

d. Scaling the datasets.

 + After preparing the data we started creating a pipeline for each model and applying it then tuned the parameter using several methods to increase train and test accuracy we took the best accuracy to be in the pipeline and we saved our model. Following are the results of the implemented models:

![accuracy](https://user-images.githubusercontent.com/109469901/215533240-45584241-5314-4050-94cb-c5fda49baf9d.jpg)


# Model Deployment using Django and Heroku:

App Link: https://team-a-model-deployment-django.herokuapp.com/
