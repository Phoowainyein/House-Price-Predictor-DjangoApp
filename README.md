# industrysoftwareProduction

This is a Django web application that provides a user-friendly interface for users to upload CSV files containing house features such as number of bedrooms, bathrooms, square footage, and more. The application utilizes a machine learning linear regression model to predict the price of a house based on these features. With the help of this application, users can easily get an estimate of the price of a house without the need for complex calculations or prior knowledge of machine learning algorithms


## Setup Virtual Environment ##

https://www.kaggle.com/code/phoonyein/virtualenvinubuntu20-04


#### Activate virtual environemnt 

```php
source venv/bin/activate
```

#### generate the requirements.txt file 

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

