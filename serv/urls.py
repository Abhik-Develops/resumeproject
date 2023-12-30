from django.urls import path
from serv.views import *

urlpatterns = [
    path('',services,name="services")
]
