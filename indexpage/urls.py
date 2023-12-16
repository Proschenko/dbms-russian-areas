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

    # region Street
    path('street_list/', views.table_street, name='street_list'),
    path('create_street/', views.create_street, name='create_street'),
    path('edit_street/<int:id_street>/', views.edit_street, name='edit_street'),
    path('delete_street/<int:id_street>/', views.delete_street, name='delete_street'),
    # endregion

    # region ResidentialBuilding
    path('residentialbuilding_list/', views.table_residentialbuilding, name='residentialbuilding_list'),
    path('create_residentialbuilding/', views.create_residentialbuilding, name='create_residentialbuilding'),
    path('edit_residentialbuilding/<int:id_residential_building>/', views.edit_residentialbuilding, name='edit_residentialbuilding'),
    path('delete_residentialbuilding/<int:id_residential_building>/', views.delete_residentialbuilding, name='delete_residentialbuilding'),
    # endregion

    # region Apartment
    path('apartment_list/', views.table_apartment, name='apartment_list'),
    path('create_apartment/', views.create_apartment, name='create_apartment'),
    path('edit_apartment/<int:id_apartment>/', views.edit_apartment, name='edit_apartment'),
    path('delete_apartment/<int:id_apartment>/', views.delete_apartment, name='delete_apartment'),
    # endregion

    # region Citizen
    path('citizen_list/', views.table_citizen, name='citizen_list'),
    path('create_citizen/', views.create_citizen, name='create_citizen'),
    path('edit_citizen/<int:id_citizen>/', views.edit_citizen, name='edit_citizen'),
    path('delete_citizen/<int:id_citizen>/', views.delete_citizen, name='delete_citizen'),
    # endregion
]
