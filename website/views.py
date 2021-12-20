from django.shortcuts import render

def index(request):
    content = {'title': 'Home Page', 'active': 'index'}
    return render(request, 'website/index.html', content)

def contact(request):
    content = {'title': 'Contact', 'active': 'contact'}
    return render(request, 'website/contact.html', content)

def about(request):
    content = {'title': 'About', 'active': 'about'}
    return render(request, 'website/about.html', content)