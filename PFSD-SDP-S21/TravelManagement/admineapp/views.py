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
                messages.info(request,"This is admin AMS page")
                return render(request,"adminhome.html")

        if flag:
            messages.info(request,"This is user's ASM page")
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

def checkinsert(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        if email==name:
            if Register.objects.filter(username=name).exists():
                messages.info(request, "username existing...")
                return render(request, "login.html")
            elif Register.objects.filter(email=email).exists():
                messages.info(request, "email existing...")
                return render(request, "index.html")
            else:
                user = Register.objects.create(name=name, email=email)
                user.save()
                messages.info(request, "user created...")
                return render(request, "login.html")
        else:
            messages.info(request, "Data inserted Successfully")
            return render(request, "index.html")
def checkupdate(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        if email==name:
            if Register.objects.filter(username=name).exists():
                messages.info(request, "username existing...")
                return render(request, "login.html")
            elif Register.objects.filter(email=email).exists():
                messages.info(request, "email existing...")
                return render(request, "index.html")
            else:
                user = Register.objects.create(name=name, email=email)
                user.save()
                messages.info(request, "user created...")
                return render(request, "login.html")
        else:
            messages.info(request, "Data updated Sucessfully...")
            return render(request, "index.html")


def checkdelete(request):
    if request.method == "POST":
        id = request.POST["id"]

        if id == id:
            if Register.objects.filter(username=id).exists():
                messages.info(request, "Data Deleted")
                return render(request, "register.html")
            elif Register.objects.filter(id=id).exists():
                messages.info(request, "email existing...")
                return render(request, "index.html")
            else:
                user = Register.objects.create(name=id)
                user.save()
                messages.info(request, "user created...")
                return render(request, "login.html")
        else:
            messages.info(request, "Data deleted Sucessfully...")
            return render(request, "index.html")
def checkinsertvehicle(request ):
    if request.method == "POST":
        name = request.POST["name"]
        id= request.POST["name"]
        if id == id:
            if Register.objects.filter(username=name).exists():
                messages.info(request, "Data Inserted Successfully")
                return render(request, "updatevehicle.html")
            elif Register.objects.filter(id=id).exists():
                messages.info(request, "already the Details of the car have been inserted")
                return render(request, "login.html")
            else:
                user = Register.objects.create(name=id)
                user.save()
                messages.info(request, "Data created...")
                return render(request, "login.html")

        else:
            messages.info(request, "Insert the data carefully")
            return render(request, "login.html")

def checkupdatevehicle(request):
    if request.method == "POST":
        name = request.POST["name"]
        id= request.POST["name"]
        if name == name:
            if Register.objects.filter(username=name).exists():
                messages.info(request, "Data updated Successfully")
                return render(request, "deletevehicle.html")
            elif Register.objects.filter(id=name).exists():
                messages.info(request, "The details have been updated")
                return render(request, "login.html")
            else:
                user = Register.objects.create(name=name)
                user.save()
                messages.info(request, "Data Updated...")
                return render(request, "login.html")

        else:
            messages.info(request, "Update the data carefully")
            return render(request, "login.html")



def checkdeletevehicle(request):
    if request.method == "POST":
        id= request.POST["name"]
        if id == id:
            if Register.objects.filter(username=id).exists():
                messages.info(request, "Data deleted Successfully")
                return render(request, "insertvehicle.html")
            elif Register.objects.filter(id=id).exists():
                messages.info(request, "The details have been deleted")
                return render(request, "login.html")
            else:
                user = Register.objects.create(name=id)
                user.save()
                messages.info(request, "Data Deleted..")
                return render(request, "login.html")

        else:
            messages.info(request, "Delete the data carefully")
            return render(request, "login.html")
def checkfeedback(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        if email==name:
            if Register.objects.filter(username=name).exists():
                messages.info(request, "Inserted Successfully..")
                return render(request, "update.html")
            elif Register.objects.filter(email=email).exists():
                messages.info(request, "email existing...")
                return render(request, "index.html")
            else:
                user = Register.objects.create(name=name, email=email)
                user.save()
                messages.info(request, "user created...")
                return render(request, "login.html")
        else:
            messages.info(request, "Data inserted Successfully...")
            return render(request, "login.html")
