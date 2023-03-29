from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from random import randrange
# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:

        try:
            u_obj = user.objects.get(email = request.POST['eee'])
            return render(request, 'register.html', {'jenil':'email is Already Registered!!!'})
        except:
            if request.POST['password'] == request.POST['REpassword']:
                global c_otp, f, e, p
                f = request.POST['qwerty']
                e = request.POST['eee']
                p = request.POST['password']

                c_otp = randrange(100000,999999)
                send_mail(
                    'Welcome',
                    f'your OTP is {c_otp}',
                    settings.EMAIL_HOST_USER,
                    [request.POST['eee']])
                return render(request, 'otp.html')
            else:
                return render(request, 'register.html',{'jenil':'both password do no match!!!'})
            
def otp_function(request):
    if str(c_otp) == request.POST['ootp']:
        user.objects.create(
            full_name = f,
            email = e,
            password = p
        )
        return render(request,'register.html', {'jenil':'Successfully Registered!!'})
    else:
        return render(request, 'otp.html',{'k':'Wrong OTP !!'})
