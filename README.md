# House Price Estimation Software

This is a Django web application that provides a user-friendly interface for users to upload CSV files containing house features such as number of bedrooms, bathrooms, square footage, and more. The application utilizes a machine learning linear regression model to predict the price of a house based on these features. With the help of this application, users can easily get an estimate of the price of a house without the need for complex calculations or prior knowledge of machine learning algorithms.


## Features
* Upload CSV file: Users can upload a CSV file containing data to train the house price estimation model. 

* Select fields for training: Users can select fields for training the model from the uploaded CSV file.The software will dynamically show only fields that were in the file.

* Train model: The model will be trained with the selected fields.

* Predict house price: Users can input a zip code, square meters, acre size, and the number of bedrooms and bathrooms to get a predicted house price.

## Usage

* Upload page: User can upload a valid CSV file that contains house data and price.

* Train page: Users can select fields for training the model from the uploaded CSV file, and the model will be trained with the selected fields.

* Predict page: Users can input a zip code, square meters, acre size, and the number of bedrooms and bathrooms to get a predicted house price.


## Setup Virtual Environment ##

https://www.kaggle.com/code/phoonyein/virtualenvinubuntu20-04


#### Activate virtual environemnt 

```php
source venv/bin/activate
```

#### Generate the requirements.txt 

```php
pip install -r requirements.txt
```

####  To ensure that  database schema is always up-to-date

```php
python manage.py migrate 
```
####  Start a local development server

```php
python manage.py runserver
```

![Alt Text](/home/phoo/industrysoftwareProduction/ezgif.com-optimize.gif)
