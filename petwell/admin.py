from django.contrib import admin
from django.db import models
from .models import Customer,Seller,Admin,Health,Booking,Adoption,Petservice,Service,Doctor,Purchase,Product,Pet

admin.site.register(Customer)
admin.site.register(Seller)
admin.site.register(Admin)
admin.site.register(Health)
admin.site.register(Booking)
admin.site.register(Adoption)
admin.site.register(Petservice)
admin.site.register(Service)
admin.site.register(Doctor)
admin.site.register(Purchase)
admin.site.register(Product)
admin.site.register(Pet)