from django.http import HttpResponse
from django.shortcuts import render

from .models import Admin,Register,Packages
from django.contrib import messages

def TravelManagementhome(request):
    return render(request, "TravelManagementhome.html")
def checkadminlogin(request):
    if request.method == "POST":
        name = request.POST["uname"]  # gets user name
        pwdd = request.POST["pwd"]
        flag = Register.objects.filter(username=name, password=pwdd).values()
        if flag:  # flag is not empty
            if name=="Nikhitha":  #Nikhitha is a admin
                messages.info(request,"This is admin TTM page")
                return render(request,"adminhome.html")

        if flag:
            messages.info(request,"This is user's TTM page")
            return render(request, "TravelManagementhome.html")
        else:
            messages.info(request, "Your credentials are not correct")
            return render(request,"loginfail.html")

def checkregistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        addr = request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]
        if pwd == cpwd:
            if Register.objects.filter(username=uname).exists():
                messages.info(request, "username existing ....")
                return render(request,"register.html")
            elif Register.objects.filter(email=email).exists():
                messages.info(request, "email existing ...")
                return render(request, "register.html")
            else:
                user = Register.objects.create(name=name,address=addr,email=email,phno=phno,username=uname,password=pwd,)
                user.save()
                messages.info(request, "user created...")
                return render(request,"login.html")
        else:
            messages.info(request, "password is not matching....")
            return render(request,"register.html")
def checkpackages(request):
    messages.info(request, "Insert the data into the Table")
    return render(request,"package.html")
def viewplaces(request):
    data = Packages.objects.all()
    return render(request,"viewplaces.html",{"placesdata":data})
def checkchangePassword(request):
    if request.method == "POST":
        uname = request.POST["uname"] # get username,old password,new password from html file
        opwd = request.POST["opwd"]
        npwd = request.POST["npwd"]
        flag=Register.objects.filter(usernmae=uname,password=opwd).values() #  filter:the html data with table row,Retrive
        if flag:
            Register.objects.filter(usernmae=uname,password=opwd).update(password=npwd) # Update
            messages.info(request, "Password Updated")
            return render(request,"ïndex.html")
        else:

            return render(request, "ïndex.html")
    else:
            return render(request,"changepassword.html")
def logout(request):
    messages.info(request,"Logout")
    return render(request,"index.html")