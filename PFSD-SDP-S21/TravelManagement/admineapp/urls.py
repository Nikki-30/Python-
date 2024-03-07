from django.urls import path
from . import views

urlpatterns=[
    path("TravelManagementthome",views.TravelManagementhome,name="TravelManagementhome"),
    path("checkadminlogin",views.checkadminlogin,name="checkadminlogin"),
    path("checkregistration",views.checkregistration,name="checkregistration"),
    path("checkpackages", views.checkpackages, name="checkpackages"),
    path("viewsplaces",views.viewplaces,name="viewplaces"),
    path("changepassword",views.checkchangePassword,name="changepassword"),
    path("logout",views.logout,name="logout"),
]
