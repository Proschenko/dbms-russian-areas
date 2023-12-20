from datetime import timezone

from django import forms
from .models import Area, City, District, Street, ResidentialBuilding, Apartment, Citizen
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['name_area', 'subject_code']
        labels = {'name_area': 'Название области',
                  'subject_code': 'Код региона'}


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name_city', 'postal_code', 'area']
        labels = {
            'name_city': 'Название города',
            'postal_code': 'Почтовый индекс',
            'area': 'Область',

        }


class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = ['name_district', 'city']
        labels = {
            'name_district': 'Название района',
            'city': 'Город'
        }


class StreetForm(forms.ModelForm):
    class Meta:
        model = Street
        fields = ['name_street', 'district']
        labels = {
            'name_street': 'Название улицы',
            'district': 'Район'
        }


class ResidentialBuildingForm(forms.ModelForm):

    def clean_area(self):
        year_of_construction = self.cleaned_data['year_of_construction']
        if year_of_construction < 1800:
            raise ValidationError(_('Дом не может быть построен ранее 1800 года'))
        return year_of_construction

    def clean_house_number(self):
        house_number = self.cleaned_data['house_number']
        if house_number < 0:
            raise ValidationError(_('Площадь не может быть отрицательной'))
        return house_number

    def clean_numbers_of_floors(self):
        numbers_of_floors = self.cleaned_data['numbers_of_floors']
        if numbers_of_floors < 0:
            raise ValidationError(_('Количество этажей не может быть отрицательной'))
        return numbers_of_floors
    class Meta:
        model = ResidentialBuilding
        fields = ['house_number', 'year_of_construction', 'numbers_of_floors', 'street']
        labels = {
            'house_number': 'Номер дома',
            'year_of_construction': 'Год постройки',
            'numbers_of_floors': 'Количество этажей',
            'street': 'Улица'
        }


class ApartmentForm(forms.ModelForm):
    def clean_area(self):
        area = self.cleaned_data['area']
        if area < 0:
            raise ValidationError(_('Площадь квартиры не может быть отрицательной'))
        return area

    def clean_apartment_number(self):
        apartment_number = self.cleaned_data['apartment_number']
        if apartment_number < 0:
            raise ValidationError(_('Номер квартиры не может быть отрицательной'))
        return apartment_number
    def clean_num_of_rooms(self):
        num_of_rooms = self.cleaned_data['area']
        if num_of_rooms < 0:
            raise ValidationError(_('Количество комнат не может быть отрицательной'))
        return num_of_rooms

    class Meta:
        model = Apartment
        fields = ['apartment_number', 'num_of_rooms', 'area', 'residential_building']
        labels = {
            'apartment_number': 'Номер квартиры',
            'num_of_rooms': 'Количество комнат',
            'area': 'Площадь',
            'residential_building': 'Номер дома',
        }


class CitizenForm(forms.ModelForm):
    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth > timezone.now().date():
            raise ValidationError(
                'Дата рождения не может быть в будущем',
                code='invalid',
                params={'value': date_of_birth},
            )
        return date_of_birth
    class Meta:
        model = Citizen
        fields = ['full_name', 'passport_data', 'phone_number', 'date_of_birth', 'gender', 'apartment']
        labels = {
            'full_name': 'Полное имя',
            'passport_data': 'Паспортные данные',
            'phone_number': 'Номер телефона',
            'date_of_birth': 'Дата рождения (ДД.ММ.ГГГГ)',
            'gender': 'Пол',
            'apartment': 'Номер квартиры',

        }
        widgets = {
            'gender': forms.RadioSelect(choices=((True, 'Мужской'), (False, 'Женский'))),
        }



class DeleteTypeForm(forms.Form):
    delete_types = [
        ('SET NULL', 'SET NULL'),
        ('CASCADE', 'CASCADE')
    ]
    delete_type = forms.ChoiceField(choices=delete_types, label='Тип удаления')
