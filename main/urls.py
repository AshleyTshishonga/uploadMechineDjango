from django.urls import path, include
from django.contrib import admin


#import from views of webapp
from . import views

urlpatterns=[
    path('', views.home, name='index'),
     path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
     path('index2', views.index2, name='index2'),
      path('upload.html',  include('csvs.urls')),
   
      
    path('signout', views.signout, name='signout'),
   
  

 
]