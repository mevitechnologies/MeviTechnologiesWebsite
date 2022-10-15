from pydoc import doc
from turtle import setundobuffer
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    if request.method=='post':
        name = request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        return render(request,'contact.html',{'name':name})
    else:
         return render(request,'contact.html',{})