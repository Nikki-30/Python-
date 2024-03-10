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
def insertPage(request):
    return render(request,"insert.html")
def updatepage(request):
    return render(request,"update.html")

def deletepage(request):
    return render(request,"delete.html")

def navbarpage(request):
    return render(request,"navbar.html")


def insertvehiclepage(request):
    return render(request,"insertvehicle.html")

def updatevehiclepage(request):
    return render(request,"updatevehicle.html")

def deletevehiclepage(request):
    return render(request,"deletevehicle.html")

def feedbackpage(request):
    return render(request,"feedback.html")



