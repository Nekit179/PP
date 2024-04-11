import django.db.models.deletion
from django.db import models

class Users(models.Model):
    login = models.CharField(max_length=100, null=False, default='')
    password = models.CharField(max_length=100, null=False, default='')
# Create your models here.

class Warehouses(models.Model):
    warehouse_id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=50, null=False, default='')

class Makers(models.Model):
    maker_id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=50, null=False, default='')
    countrt = models.CharField(max_length=50, null=False, default='')
    description = models.TextField(null=False, default='')

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=50, null=False, default='')

class Goods(models.Model):
    good_id = models.IntegerField(primary_key=True, null=False)

    maker_id = models.ForeignKey('Makers', on_delete=django.db.models.deletion.PROTECT)
    warehouse_id = models.ForeignKey('Warehouses', on_delete=django.db.models.deletion.PROTECT)
    category_id = models.ForeignKey('Category', on_delete=django.db.models.deletion.PROTECT)
    name = models.CharField(max_length=50, null=False, default='')
    description = models.TextField(null=False, default='')
    count = models.IntegerField(null=False)
    price = models.FloatField(null=True)
