# Prediction-of-startup-acquisition-status 
The dataset is all about the Startup's Financial Information and we  need to predict the current financial Status of company. The database is of Crunchbase-2013, database, company, investors and all the others details belongs to the company. In this project, we analyzed the company's status i.e, Operating , Acquired, ipo or closed.

# Understand the Dataset

- Dataset Link: ( https://drive.google.com/file/d/17bfNyMgP-PofCkdlvnLHxxFqV8mdDo-9/view )
* The dataset is completely based ont the company's information from company's website of 2013.
+ Features: All the columns with  the comapny's infromatiom like name, permalink, category, funding dates, funding rounds, funding amounts, city, state, last milestone dates many more.
- Target variable: Status

# Data Cleaning
+ We deleted with redundancy, granuality and irrelevant information we also deleted instances with missing values for specific columns basically we removed NULL values for the following columns status, country_code, Founded_at. For the columns with les percentage of NULL values with used the imputing method using mean, median and mode.


# Data Transformation
* Here we are fixing irrelevant data types to some columns so we converted columns the included data year datatype.

- Then we started filling the NULL values in closed_at for calculation of the age of company then we created column active_days from substrating colsed_at fro, founded _at then we removed rows with negative values in active_days and dropped the other two columns.

+ Then we removed outliers using IQR method then we generalized category_code and country_code using One hot encoder to prepare for feature engineering through working on our targetd variable Status and we finalized the data analysis part with deleting duplicates from datasets.


# Model Building

* We started the ML part through applying LOgistic Regressinn Model, XGBoost Classifier Model, Quadratic Analysis Model and Random Foresr Classifier Model. BUt first we had to prepare the data through the following steps.

a. Splitting the data. We split the data through SKlearn using test_train_split function.

b. Seprating numerical and categorical columns.

c. Applying one-hot encoding to the whole columns.

d. Scaling the datasets.

 + After preparing the data we started created a pipeline for each model an dapplying it then tuned the parameter using several methods to increase train and test accuracy and we took the best accuracy to be in the pipeline and we saved our model. Following are results of implemeted models:

![accuracy](https://user-images.githubusercontent.com/109469901/215533240-45584241-5314-4050-94cb-c5fda49baf9d.jpg)


# Model Deployment using Django and Heroku:

App Link: https://team-a-model-deployment-django.herokuapp.com/
