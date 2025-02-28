from django.urls import path
from . import views
from django.urls import path
from .views import contact_submit

app_name = 'honyakuapp'

urlpatterns = [
    path('', views.main_view, name='main'),
    path('', views.form_view, name='form'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
    path('contact/sent/', views.contact_sent, name='contact_sent'),
]
