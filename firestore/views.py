from django.shortcuts import render

def view_name(request):
    return render(request, 'template_name.html', {})