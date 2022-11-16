import os
import pyrebase
from django.shortcuts import render
from dotenv import load_dotenv

# the load_dotenv function gets the environment variables defined in .env file
load_dotenv()

#firebase config
config = {
    "apiKey": "AIzaSyDYU7Ry7YnlfvBl4LKIork_AIcRTDZ3gGE",
    "authDomain": "jls-react.firebaseapp.com",
    "databaseURL": "https://jls-react-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "jls-react",
    "storageBucket": "jls-react.appspot.com",
    "messagingSenderId": "599654946369",
    "appId": "1:599654946369:web:800da4c47682174c34d8c0",
    "databaseURL": "",
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()


def view_name(request):
    if request.method == 'POST':
        file = request.FILES['file']
        file_save = default_storage.save(file.name, file)
        storage.child("files/" + file.name).put("media/" + file.name)
        delete = default_storage.delete(file.name)
        messages.success(request, "File upload in Firebase Storage successful")
        return redirect('main')
    else:
        return render(request, 'fire.html')