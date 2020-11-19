from django.urls import path
from . import views
from django.contrib import auth


urlpatterns = [
    path('',views.login),
    path('home/',views.home),
    path('signup/',views.signup),
    path('register/',views.handlesignup),
]
