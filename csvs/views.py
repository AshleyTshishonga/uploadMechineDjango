
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import path
from .forms import CsvModelForm
import csv
from django.contrib.auth.models import User,auth
from django.contrib.auth.models import User,auth
from .models import Csv
import csv



# Create your views here.
def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=True)
        context={'file':Csv.objects.all()}
        return render(request, 'csvs/upload.html',{'form': form}) 
  
    else:
        return render(request, 'csvs/upload.html',{'form': form}) 