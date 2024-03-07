from django.shortcuts import render


def homepage(request):
    return render(request, "index.html")

def loginpage(request):
    return render(request, "login.html")

def aboutpage(request):
    return render(request, "about.html")

def contactpage(request):
    return render(request, "contact.html")

def registrationPage(request):
    return render(request,"register.html")

