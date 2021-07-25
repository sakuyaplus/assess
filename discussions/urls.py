from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='discussions'),
    path('dcomment', views.dcomment, name='dcomment'),
    path('delcomment', views.delcomment, name='delcomment')
]