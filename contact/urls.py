from django.urls import path

from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.contact, name='contact'),
    path('email/',views.email,name='email'),
]