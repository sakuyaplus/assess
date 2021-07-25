from django.urls import path
from . import views

urlpatterns = [
    path('ccomment', views.ccomment, name='ccomment'),
    path('', views.delccomment, name='delccomment')
]