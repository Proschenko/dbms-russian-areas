# Generated by Django 4.2.7 on 2023-12-14 15:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id_apartment', models.AutoField(primary_key=True, serialize=False)),
                ('apartment_number', models.CharField(max_length=50, validators=[django.core.validators.MaxLengthValidator(50)])),
                ('num_of_rooms', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('area', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id_area', models.AutoField(primary_key=True, serialize=False)),
                ('name_area', models.CharField(max_length=255)),
                ('subject_code', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(999)])),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id_city', models.AutoField(primary_key=True, serialize=False)),
                ('name_city', models.CharField(max_length=255)),
                ('postal_code', models.IntegerField(validators=[django.core.validators.MinValueValidator(100000), django.core.validators.MaxValueValidator(999999)])),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexpage.area')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id_district', models.AutoField(primary_key=True, serialize=False)),
                ('name_district', models.CharField(max_length=100, validators=[django.core.validators.MaxLengthValidator(100)])),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexpage.city')),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id_street', models.AutoField(primary_key=True, serialize=False)),
                ('name_street', models.CharField(max_length=255)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexpage.district')),
            ],
        ),
        migrations.CreateModel(
            name='ResidentialBuilding',
            fields=[
                ('id_residential_building', models.AutoField(primary_key=True, serialize=False)),
                ('house_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)])),
                ('year_of_construction', models.IntegerField(validators=[django.core.validators.MinValueValidator(1800)])),
                ('numbers_of_floors', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(300)])),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexpage.street')),
            ],
        ),
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id_citizen', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('passport_data', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=11)),
                ('date_of_birth', models.DateField()),
                ('gender', models.BooleanField()),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexpage.apartment')),
            ],
        ),
        migrations.AddField(
            model_name='apartment',
            name='residential_building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexpage.residentialbuilding'),
        ),
    ]