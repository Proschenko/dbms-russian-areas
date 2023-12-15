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
]
