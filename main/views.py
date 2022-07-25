from pyexpat.errors import messages
from . import views
from email import message
from math import remainder
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, "index.html")


def signup(request):
   if request.method == 'POST':

        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

     
        new_user = User.objects.create_user(username,email,password1)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()
      
        return redirect("signin")
   else:
              
      return render(request,"signup.html")
 
 
        #return redirect('signup.html')
def signin(request):
      if request.method == 'POST':
       
       
         username = request.POST['username']
         password = request.POST['password']
      
         user = auth.authenticate(username=username,password=password) 
         
         if user is not None:
      
               auth.login(request, user)
              
               return redirect("upload.html")
               #return redirect("index")
               #return render(request,"signup.html")
               #return render(request, "signin") 
         else:
              
             # message.info(request,"Bad Credentials")
              return redirect("signin")
               #return redirect("/")
            # return render(request,"signin.html")
      
            #return render(request,"signup.html")
      else:
               return render(request,"signin.html")


def signout(request):
      auth.logout(request)
      #messages.success(request,"logout ")
      return render(request,"signin.html")

def index2(request):
      context = {
            'user' : request.user
      }
      # user_id= current_user.id
      # user_first_name= current_user.first_name
      # print(user_id)
      # context = {'user_id': user_id, 'user_first_name': user_first_name}
      return render(request, "index2.html", context)
