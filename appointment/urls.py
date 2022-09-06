from django.urls import path
from . import views

app_name = 'appointment'
urlpatterns = [
    path('', views.addAppoint, name="Appointment Booking")
]