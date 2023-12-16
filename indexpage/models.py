from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.dispatch import receiver
from django.db.models.signals import post_save



@receiver(post_save, sender=User)
def user_saved(sender, instance, created, **kwargs):
    instance.request = HttpRequest()


class Area(models.Model):
    id_area = models.AutoField(primary_key=True)
    name_area = models.CharField(max_length=255)
    subject_code = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999)])


    def __str__(self):
        return self.name_area

class City(models.Model):
    id_city = models.AutoField(primary_key=True)
    name_city = models.CharField(max_length=255)
    postal_code = models.IntegerField(validators=[MinValueValidator(100000), MaxValueValidator(999999)])
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name_city}, {self.area.name_area}"

class District(models.Model):
    id_district = models.AutoField(primary_key=True)
    name_district = models.CharField(max_length=100, validators=[MaxLengthValidator(100)])
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_district

class Street(models.Model):
    id_street = models.AutoField(primary_key=True)
    name_street = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_street

class ResidentialBuilding(models.Model):
    id_residential_building = models.AutoField(primary_key=True)
    house_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    year_of_construction = models.IntegerField(validators=[MinValueValidator(1800)])
    numbers_of_floors = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(300)])
    street = models.ForeignKey(Street, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.house_number)

class Apartment(models.Model):
    id_apartment = models.AutoField(primary_key=True)
    apartment_number = models.CharField(max_length=50, validators=[MaxLengthValidator(50)])
    num_of_rooms = models.IntegerField(validators=[MinValueValidator(1)])
    area = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    residential_building = models.ForeignKey(ResidentialBuilding, on_delete=models.CASCADE)

    def __str__(self):
        return self.apartment_number

class Citizen(models.Model):
    id_citizen = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    passport_data = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=11)
    date_of_birth = models.DateField()
    gender = models.BooleanField()
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
