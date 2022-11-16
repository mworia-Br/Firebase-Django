import os
import pyrebase
from django.shortcuts import render
from dotenv import load_dotenv

# the load_dotenv function gets the environment variables defined in .env file
load_dotenv()

#firebase config


def view_name(request):
    return render(request, 'fire.html', {})