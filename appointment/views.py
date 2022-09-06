from django.shortcuts import render
from .models import Registration

def addAppoint(request):
    if request.method=="POST":
        post=Registration()
        post.name_patient=request.POST['name_patient']
        post.contact_no=request.POST['contact_no']
        post.date=request.POST['date']
        post.name_doctor=request.POST['name_doctor']
        post.save()
        return render(request, 'appointment/index.html')
    else:
        return render(request, 'appointment/index.html')