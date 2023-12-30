from django.shortcuts import render, redirect
from .models import FeedBack

# Create your views here.

def home(request):
    context = {'home' : 'active'}
    return render(request,'core/home.html',context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        msg = request.POST['message']
        obj = FeedBack(name=name, email=email, subject=subject, message=msg)
        obj.save()
        return redirect("/thankyou")
    context = {'contact' : 'active'}
    return render(request,'core/contact.html',context)

def thankyou(request):
    return render(request, 'core/thankyou.html')