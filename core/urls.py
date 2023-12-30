from django.urls import path
from core.views import *

urlpatterns = [
    path('',home,name="home"),
    path('contact/',contact,name="contact"),
    path('thankyou/',thankyou,name="thankyou"),
]
