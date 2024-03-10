from django.urls import path
from . import views

urlpatterns=[
    path("TravelManagementthome",views.TravelManagementhome,name="TravelManagementhome"),
    path("checkadminlogin",views.checkadminlogin,name="checkadminlogin"),
    path("checkregistration",views.checkregistration,name="checkregistration"),
    path("checkpackages", views.checkpackages, name="checkpackages"),
    path("viewsplaces",views.viewplaces,name="viewplaces"),
    path("changepassword",views.checkchangePassword,name="changepassword"),
    path("checkinsert",views.checkinsert,name="checkinsert"),
    path("checkupdate",views.checkupdate, name="checkupdate"),
    path("checkdelete",views.checkdelete, name="checkdelete"),
    path("checkinsertvehicle",views.checkinsertvehicle, name="checkinsertvehicle"),
    path("checkupdatevehicle",views.checkupdatevehicle, name="checkupdatevehicle"),
    path("checkdeletevehicle",views.checkdeletevehicle, name="checkdeletevehicle"),
    path("checkfeedback",views.checkfeedback, name="checkfeedback"),
    path("logout",views.logout,name="logout"),
]
