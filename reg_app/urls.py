from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('ootp/', otp_function, name = 'otp_url')
]