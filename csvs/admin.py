from django.contrib import admin
from .models import Csv
from django.http import HttpResponse


# Register your models here.

admin.site.register(Csv) 