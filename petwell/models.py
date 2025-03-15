from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Customer(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    password = models.CharField(max_length=250)
    address = models.CharField(max_length=650,null=True)
    phone =  models.CharField(max_length=250)

class Pet(models.Model):
    petid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    age = models.IntegerField()
    gender = models.CharField(max_length=300)
    animal = models.CharField(max_length=300)
    breed = models.CharField(max_length=300)
    color = models.CharField(max_length=300)
    customer_id = models.ForeignKey(Customer,default=1,on_delete=models.DO_NOTHING)

class Doctor(models.Model):
    doctorid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    phone =  models.CharField(max_length=250)
    qualification =  models.CharField(max_length=250)
    email = models.CharField(max_length=300)
    password = models.CharField(max_length=250)

class Service(models.Model):
    serviceid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    cost = models.IntegerField()
    time = models.CharField(max_length=300)

class Petservice(models.Model):
    pserviceid = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer,default=1,on_delete=models.DO_NOTHING)
    service_id = models.ForeignKey(Service,default=1,on_delete=models.DO_NOTHING)
    pet_id = models.ForeignKey(Pet,default=1,on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=300)

class Adoption(models.Model):
    aid = models.AutoField(primary_key=True)
    breed = models.CharField(max_length=300)
    animal = models.CharField(max_length=300)
    color = models.CharField(max_length=300)
    age = models.IntegerField()
    description = models.CharField(max_length=650,null=True)
    image = models.CharField(max_length=300)
    gender = models.CharField(max_length=300)
    adopted = models.BooleanField(default=False)

class Booking(models.Model):
    bid = models.AutoField(primary_key=True)    
    doctor_id = models.ForeignKey(Doctor,default=1,on_delete=models.DO_NOTHING)
    customer_id =  models.ForeignKey(Customer,default=1,on_delete=models.DO_NOTHING)
    pet_id =  models.ForeignKey(Pet,default=1,on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    slot = models.CharField(max_length=300)
    booking_type = models.CharField(max_length=300)

class Health(models.Model):
    hid = models.AutoField(primary_key=True) 
    pet_id =  models.ForeignKey(Pet,default=1,on_delete=models.DO_NOTHING)
    customer_id =  models.ForeignKey(Customer,default=1,on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    description = models.CharField(max_length=650,null=True)
    prescription = models.CharField(max_length=650,null=True)

class Admin (models.Model):
    aid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=300)
    password = models.CharField(max_length=250)

class Seller (models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=300)
    password = models.CharField(max_length=250)

class Product(models.Model):
    productid = models.AutoField(primary_key=True)
    seller_id = models.ForeignKey(Seller,default=1,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    quantity = models.IntegerField()
    animal = models.CharField(max_length=300)
    producttype = models.CharField(max_length=300)
    rating = models.IntegerField()
    approved = models.BooleanField(default=False)

class Purchase(models.Model):
    purchaseid = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    paid = models.BooleanField(default=False)
    delivery_status = models.CharField(max_length=300)
    product_id = models.ForeignKey(Product,default=1,on_delete=models.DO_NOTHING)
    customer_id = models.ForeignKey(Customer,default=1,on_delete=models.DO_NOTHING)
