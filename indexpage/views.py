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
def table_area(request):
    area = Area.objects.all().order_by('id_area')
    context = {
        'area': area,

    }
    return render(request, 'indexpage/table_area.html', context)



def create_area(request):
    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(table_area)  # Замените 'your_view_name' на имя вашего представления
    else:
        form = AreaForm()
    # TODO поменяй index.html
    return render(request, 'indexpage/index.html', {'form': form})

def edit_area(request,area_id):
    area = get_object_or_404(Area, pk=area_id)

    if request.method == 'POST':
        form = AreaForm(request.POST, instance=area)
        if form.is_valid():
            form.save()
            my_signal.send(sender=area, request=request)
            return redirect(table_area)  # Замените 'your_view_name' на имя вашего представления
    else:
        form = AreaForm(instance=area)
    # TODO поменяй index.html
    return render(request, 'indexpage/index.html', {'form': form, 'area': area})



def delete_area(request, area_id):
    area = get_object_or_404(Area, pk=area_id)
    if request.method == 'POST':
        delete_type_form = DeleteTypeForm(request.POST)
        if delete_type_form.is_valid():
            delete_type = delete_type_form.cleaned_data['delete_type']
            if delete_type == 'CASCADE':
                area.delete()
                return redirect(table_area)

            else:
                # Ваш запрос SQL
                delete_sport_type_sql = f"DELETE FROM indexpage_area WHERE area_id = {area_id}"

                # Выполнение запроса
                with connection.cursor() as cursor:
                    cursor.execute(delete_sport_type_sql)

                return redirect(table_area())

    else:
        delete_type_form = DeleteTypeForm()
    # TODO поменяй index.html
    return render(request, 'indexpage/index.html',
                  {'delete_type_form': delete_type_form, 'area_id': area_id})



