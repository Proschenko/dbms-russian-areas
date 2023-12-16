from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),

    # region Area
    path('area_list/', views.table_area, name='area_list'),
    path('create_area/', views.create_area, name='create_area'),
    path('edit_area/<int:id_area>/', views.edit_area, name='edit_area'),
    path('delete_area/<int:id_area>/', views.delete_area, name='delete_area'),
    # endregion

    # region City
    path('city_list/', views.table_city, name='city_list'),
    path('create_city/', views.create_city, name='create_city'),
    path('edit_city/<int:id_city>/', views.edit_city, name='edit_city'),
    path('delete_city/<int:id_city>/', views.delete_city, name='delete_city'),
    # endregion

    # region District
    path('district_list/', views.table_district, name='district_list'),
    path('create_district/', views.create_district, name='create_district'),
    path('edit_district/<int:id_district>/', views.edit_district, name='edit_district'),
    path('delete_district/<int:id_district>/', views.delete_district, name='delete_district'),
    # endregion
]
