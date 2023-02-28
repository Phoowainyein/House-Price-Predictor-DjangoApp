from django.shortcuts import render
import csv
from django.core.files.storage import default_storage

# Create your views here.
def home(request):
    return render(request,'home.html',{})




def upload_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
         # save the uploaded file to a permanent location
        file_path = default_storage.save('uploads/csv_files/%s' % csv_file.name, csv_file)
        data = csv_file.read().decode('utf-8').splitlines()
        reader = csv.reader(data)
        for row in reader:
            # Process the row as needed
            # Example: print the first cell of each row
            print(row[0])
        return render(request,'train.html',{})
    return render(request,'train.html',{})

def upload_csv_view(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        # handle the uploaded file
        csv_file = request.FILES['csv_file']
        # store the file in a location of your choice
        with open('lookup/csvstorage/{}'.format(csv_file.name), 'wb+') as destination:
            for chunk in csv_file.chunks():
                destination.write(chunk)
        # return a success response
        return HttpResponse('Upload successful.')
    else:
        # handle GET requests or requests without a file
        return render(request, 'home.html')

def train(request):
    return render(request,'train.html')