from django.urls import path, include
from .views import upload_file_view
from . import views

app_name='csvs'

urlpatterns = [
    
    path('', upload_file_view, name='upload-view'),
    
   
   
]