from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from myapp import views


urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('shilpannova/',views.shilpannova),
    path('shilpanreva/',views.shilpanreva),
    path('about/',views.about),
    path('nri/',views.nri),
    path('career/',views.career),
    path('inquiry/',views.inquiry),
    path('home/',views.home),
    path('userlogout/',views.userlogout),
    path('updateprofile/',views.updateprofile),
]