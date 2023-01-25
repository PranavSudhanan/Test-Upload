from django.urls import path
from .views import *


urlpatterns = [

    path('index/', index),
    path('register/', register)

]