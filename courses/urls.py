from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='courses'),
    path('<int:listing_id>', views.listing, name='courselisting'),
    path('search', views.search, name='coursesearch')
]