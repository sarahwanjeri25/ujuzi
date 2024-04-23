from django.urls import path,include
from . import views 
urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    ]
    # "" in path means it is the main page
