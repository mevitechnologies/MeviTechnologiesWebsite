
from django.urls import include, path
from . import views
urlpatterns = [
    
    path("index.html",views.index,name='index'),
    path("",views.index,name='index'),
    path("about.html",views.about,name='about'),
    path("services.html",views.services,name='services'),
    path("contact.html",views.contact,name='contact'),
]
