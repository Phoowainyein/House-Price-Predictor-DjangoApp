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

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pickle


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

def upload_csv(request):
    global headers
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        df = pd.read_csv(csv_file)
        headers= list(df.columns)
        print(headers)
        

        # Define the folder path to save the CSV files
        csv_folder = os.path.join(settings.BASE_DIR, 'csv_files')

        # Delete all files in the folder
        delete_files_in_folder(csv_folder)

        # Save the uploaded CSV file to the folder
        with open(os.path.join(csv_folder, csv_file.name), 'wb+') as destination:
            for chunk in csv_file.chunks():
                destination.write(chunk)
        return render(request, 'train.html', {'headers':headers})
    # else:
    #     form = UploadCSVForm()
    #     return render(request, 'home.html')


def train(request):
    return render(request,'train.html',{'headers':headers})

def train_model(request):
        if request.method == 'POST':
            selected_headers =  json.loads(request.body)['selected_headers']
            print('selected headers :',selected_headers)
            # Load your dataset
            dataset = pd.read_csv('~/industrysoftwareProduction/housepricepredictionApp/csv_files/house_zipcode_usa.csv')

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

            # Return the training performance as JsonResponse
            return JsonResponse({'message': 'Training successful!', 'mse': mse})
        else:
            # Handle the case for non-POST requests if needed
            pass

def predict(request):
    return render(request,'predict.html',{})

def predict_model(request):
    