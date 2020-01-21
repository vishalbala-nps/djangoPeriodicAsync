from django.shortcuts import render
from django.http import HttpResponse

from datetime import *
import requests
import json
# Create your views here.

def index(request):
   f = open("currentval.txt","r")
   mjson = json.load(f)
   f.close()
   print(mjson)
   return render(request,"details.html",{"n1":mjson["number1"],"n2":mjson["number2"],"ans":mjson["sum"],"date":mjson["pubDate"]})