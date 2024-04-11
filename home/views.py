from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse



# Create your views here.


def homepage(request):
    return render(request, 'home/homepage.html')


def contact_us(request):
    if request.method=="POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()
        return HttpResponse("<h1>success</h1>")
    return render(request, 'home/contact_us.html')