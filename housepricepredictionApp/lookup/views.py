from django.shortcuts import render
import os
import csv
from django.core.files.storage import default_storage
from django.conf import settings
from django.utils.text import slugify
import shutil
import pandas as pd
from django.http import JsonResponse
import json
import  re

#for training
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pickle
import numpy as np


# Create your views here.
def home(request):
    return render(request,'home.html',{})

def delete_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

def validate_csv(df):
    required_patterns = [
        r'price',
        r'zipcode|zip_code|zip-code',
        r'bathrooms?|baths?',
        r'bedrooms?|beds?'
    ]

    missing_columns = []

    for pattern in required_patterns:
        if not any(re.search(pattern, column, re.IGNORECASE) for column in df.columns):
            missing_columns.append(pattern)

    if missing_columns:
        return False, missing_columns

    # Additional validation checks can be added here

    return True, missing_columns


from django.http import JsonResponse

def upload_csv(request):
    global headers
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        df = pd.read_csv(csv_file)
        headers= list(df.columns)
        print(headers)
        is_valid, missing_columns = validate_csv(df)

        if not is_valid:
            error_message = 'Invalid CSV file. Please upload a CSV file containing house price data with columns: price, zip_code, bathrooms, and bedrooms. Missing columns: {}'.format(', '.join(missing_columns))
            return JsonResponse({'is_valid': False, 'error_message': error_message})

        # Define the folder path to save the CSV files
        csv_folder = os.path.join(settings.BASE_DIR, 'csv_files')

        # Delete all files in the folder
        delete_files_in_folder(csv_folder)

        # Save the uploaded CSV file to the folder
        with open(os.path.join(csv_folder, 'uploadedcsv.csv'), 'wb+') as destination:
            for chunk in csv_file.chunks():
                destination.write(chunk)
        return JsonResponse({'is_valid': True})




# def upload_csv(request):
#     global headers
#     if request.method == 'POST' and request.FILES['csv_file']:
#         csv_file = request.FILES['csv_file']
#         df = pd.read_csv(csv_file)
#         headers= list(df.columns)
#         print(headers)
#         is_valid, missing_columns = validate_csv(df)

#         if not is_valid:
#             error_message = 'Invalid CSV file. Please upload a CSV file containing house price data with columns: price, zip_code, bathrooms, and bedrooms. Missing columns: {}'.format(', '.join(missing_columns))
#             return JsonResponse({'error': True, 'error_message': error_message})
#             #return render(request, 'home.html', {'error_message': error_message})

        
            
#             # Define the folder path to save the CSV files
#             csv_folder = os.path.join(settings.BASE_DIR, 'csv_files')

#             # Delete all files in the folder
#             delete_files_in_folder(csv_folder)

#             # Save the uploaded CSV file to the folder
#             with open(os.path.join(csv_folder, 'uploadedcsv.csv'), 'wb+') as destination:
#                 for chunk in csv_file.chunks():
#                     destination.write(chunk)
#             return render(request, 'train.html', {'headers':headers})
   


def train(request):
    return render(request,'train.html',{'headers':headers})

def train_model(request):
        if request.method == 'POST':
            selected_headers =  json.loads(request.body)['selected_headers']
            print('selected headers :',selected_headers)
            # Load your dataset
            dataset = pd.read_csv('~/industrysoftwareProduction/housepricepredictionApp/csv_files/uploadedcsv.csv')

            # Filter the dataset with the selected headers and target variable
            X = dataset[selected_headers]
            y = dataset['price']  # Replace 'target_variable' with the name of your target column

            # Split the dataset into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Train the Linear Regression model
            model = LinearRegression()
            model.fit(X_train, y_train)

            # Calculate the training performance
            y_pred = model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)

            # Save the trained model for later use
            with open('trained_model.pkl', 'wb') as f:
                pickle.dump(model, f)
            # Save the selected headers for later use
            with open(os.path.join(settings.BASE_DIR, 'selected_headers.json'), 'w') as f:
                json.dump(selected_headers, f)

            # Return the training performance as JsonResponse
            return JsonResponse({'message': 'Training successful!', 'mse': mse})
        else:
            # Handle the case for non-POST requests if needed
            pass


def map_input_array(input_array, selected_headers, headers):
    mapped_array = []
    for header in selected_headers:
        index = headers.index(header)
        numeric_value = pd.to_numeric(input_array[index], errors='coerce')
        mapped_array.append(numeric_value)
        
    return np.array(mapped_array)




def predict(request):
    return render(request,'predict.html',{})

def predict_model(request):
    
    zip_code = request.GET.get('n1')
    square_meters = request.GET.get('n2')
    acre_size = request.GET.get('n3')
    num_bedrooms = request.GET.get('n4')
    num_bathrooms = request.GET.get('n5')
    print(zip_code)

    # Load the trained model
    with open(os.path.join(settings.BASE_DIR,  'trained_model.pkl'), 'rb') as f:
        model = pickle.load(f)

    #Load the selected headers for the trained model
    with open(os.path.join(settings.BASE_DIR, 'selected_headers.json'), 'r') as f:
        selected_headers = json.load(f)

      # Create the input array for prediction
    input_array = [zip_code, square_meters, acre_size, num_bedrooms, num_bathrooms]

    # Map the input array to the selected columns used for training the model
    mapped_input_array = map_input_array(input_array, selected_headers, headers)

    # Make a prediction using the loaded model
    pred = model.predict(mapped_input_array.reshape(1, -1))[0]
    pred = round(pred)
    print('predicted price is :',pred)
    # Return the predicted price as JsonResponse
    return JsonResponse({'predicted_price': pred})
    
    
