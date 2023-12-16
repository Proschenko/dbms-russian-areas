from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string


from django.db import connection
from docx import Document
from openpyxl import Workbook
from .signals import my_signal
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
# Create your views here.
from .models import  Area, City, District, Street, ResidentialBuilding,Apartment,Citizen
from .forms import AreaForm, CityForm, DistrictForm, StreetForm, ResidentialBuildingForm, ApartmentForm, CitizenForm, DeleteTypeForm

def index_page(request):
    return render(request, 'indexpage/index.html')

# region Area
def table_area(request):
    areas = Area.objects.all().order_by('id_area')
    context = {
        'areas': areas,
    }
    return render(request, 'indexpage/table_area.html', context)

def create_area(request):
    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(table_area)
    else:
        form = AreaForm()
    return render(request, 'indexpage/create_area.html', {'form': form})

def edit_area(request, id_area):
    area = get_object_or_404(Area, pk=id_area)

    if request.method == 'POST':
        form = AreaForm(request.POST, instance=area)
        if form.is_valid():
            form.save()
            my_signal.send(sender=area, request=request)
            return redirect(table_area)
    else:
        form = AreaForm(instance=area)
    return render(request, 'indexpage/edit_area.html', {'form': form, 'area': area})



def delete_area(request, id_area):
    area = get_object_or_404(Area, pk=id_area)
    if request.method == 'POST':
        delete_type_form = DeleteTypeForm(request.POST)
        if delete_type_form.is_valid():
            delete_type = delete_type_form.cleaned_data['delete_type']
            if delete_type == 'CASCADE':
                area.delete()
                return redirect('area_list')

            else:
                # Ваш запрос SQL
                delete_area_sql = f"DELETE FROM indexpage_area WHERE id_area = {id_area}"

                # Выполнение запроса
                with connection.cursor() as cursor:
                    cursor.execute(delete_area_sql)

                return redirect('area_list')

    else:
        delete_type_form = DeleteTypeForm()

    context = {
        'delete_type_form': delete_type_form,
        'area_id': id_area,
        'area_name': area.name_area
    }
    return render(request, 'indexpage/delete_area.html', context)

# endregion
# region City
def table_city(request):
    cities = City.objects.all().order_by('id_city')
    context = {
        'cities': cities,
    }
    return render(request, 'indexpage/table_city.html', context)

def create_city(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(table_city)
    else:
        form = CityForm()
    return render(request, 'indexpage/create_city.html', {'form': form})

def edit_city(request, id_city):
    city = get_object_or_404(City, pk=id_city)

    if request.method == 'POST':
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            return redirect(table_city)
    else:
        form = CityForm(instance=city)
    return render(request, 'indexpage/edit_city.html', {'form': form, 'city': city})

def delete_city(request, id_city):
    city = get_object_or_404(City, pk=id_city)
    if request.method == 'POST':
        delete_type_form = DeleteTypeForm(request.POST)
        if delete_type_form.is_valid():
            delete_type = delete_type_form.cleaned_data['delete_type']
            if delete_type == 'CASCADE':
                city.delete()
                return redirect('city_list')
            else:
                # Ваш запрос SQL
                delete_city_sql = f"DELETE FROM indexpage_city WHERE id_city = {id_city}"

                # Выполнение запроса
                with connection.cursor() as cursor:
                    cursor.execute(delete_city_sql)

                return redirect('city_list')
    else:
        delete_type_form = DeleteTypeForm()

    context = {
        'delete_type_form': delete_type_form,
        'city_id': id_city,
        'city_name': city.name_city
    }
    return render(request, 'indexpage/delete_city.html', context)
# endregion




