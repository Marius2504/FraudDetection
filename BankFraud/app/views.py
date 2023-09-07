from django.shortcuts import render, HttpResponse
from PIL import Image
import io

def home(request):
    return render(request,'index.html',{})
