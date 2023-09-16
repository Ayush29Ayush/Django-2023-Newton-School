from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("success-page", views.success_page, name="success-page"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    
]
