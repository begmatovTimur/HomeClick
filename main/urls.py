from pydoc import visiblename
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('map', views.map, name="map"),
    path('estates/<int:pk>', views.estate_detail, name="estate_detail"),
    path('categories/<int:pk>', views.category_detail, name='category_detail'),
    path('add_estate', views.add_estate, name='add_estate')
]