from django import forms
from .models import Area, City, District, Street, ResidentialBuilding, Apartment, Citizen

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['name_area','subject_code']
        labels = {'name_area': 'Название области',
                  'subject_code': 'Код региона'}

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name_city', 'postal_code']
        labels = {
            'name_city': 'Название города',
            'postal_code': 'Почтовый индекс',
        }

class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = ['name_district']
        labels = {
            'name_district': 'Название района',
        }

class StreetForm(forms.ModelForm):
    class Meta:
        model = Street
        fields = ['name_street']
        labels = {
            'name_street': 'Название улицы',
        }

class ResidentialBuildingForm(forms.ModelForm):
    class Meta:
        model = ResidentialBuilding
        fields = ['house_number', 'year_of_construction', 'numbers_of_floors']
        labels = {
            'house_number': 'Номер дома',
            'year_of_construction': 'Год постройки',
            'numbers_of_floors': 'Количество этажей',
        }

class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['apartment_number', 'num_of_rooms', 'area']
        labels = {
            'apartment_number': 'Номер квартиры',
            'num_of_rooms': 'Количество комнат',
            'area': 'Площадь',
        }

class CitizenForm(forms.ModelForm):
    class Meta:
        model = Citizen
        fields = ['full_name', 'passport_data', 'phone_number', 'date_of_birth', 'gender' ]
        labels = {
            'full_name': 'Полное имя',
            'passport_data': 'Паспортные данные',
            'phone_number': 'Номер телефона',
            'date_of_birth': 'Дата рождения',
            'gender': 'Пол',

        }

class DeleteTypeForm(forms.Form):
    delete_types = [
        ('SET NULL', 'SET NULL'),
        ('CASCADE', 'CASCADE')
    ]
    delete_type = forms.ChoiceField(choices=delete_types, label='Тип удаления')
