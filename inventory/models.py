from django.db import models
choices=[('medical supplies','medical supplies'),('medical equipment','medical equipment'),('medications','medications')]

# Create your models here.
class Supplier(models.Model):
    name=models.CharField(max_length=300)
    contact=models.IntegerField()
    email=models.EmailField()
    def __str__(self):
        return self.name
    
class Inventory(models.Model):
    name=models.CharField(max_length=300)
    category=models.CharField(max_length=200,choices=choices)
    description=models.TextField()
    supplier=models.ForeignKey(Supplier,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name

class InventoryTrack(models.Model):
    name=models.ForeignKey(Inventory,on_delete=models.CASCADE)
    quantity_available=models.IntegerField()
    unit_price=models.IntegerField()
    total_price=models.IntegerField()
    notes=models.TextField(null=True,blank=True)
    product_in=models.IntegerField(null=True,blank=True)
    opening_numbers_of_product=models.IntegerField(null=True,blank=True)
    closing_number_of_products=models.IntegerField(null=True,blank=True)
    supplier=models.ForeignKey(Supplier,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name
