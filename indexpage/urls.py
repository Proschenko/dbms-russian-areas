from django.urls import path
from . import views



urlpatterns = [
    path('', views.index_page,name='index_page'),
    path('area_list/', views.table_area, name='area_list')
]