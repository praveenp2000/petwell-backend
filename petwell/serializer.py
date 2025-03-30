from rest_framework import serializers
from petwell.models import Customer,Pet,Admin,Product,Purchase,Doctor,Service,Petservice,Adoption,Booking,Health,Seller

class CustomerLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('email','password')

class DoctorLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('email','password')

class AdminLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('email','password')

class SellerLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ('email','password')



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('cid','name','email','password','address','phone')

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('name','phone','qualification','email','password')

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('name','email','password')

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ('name','email','password')

class EditCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name','email','password','address','phone')

class EditPetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('name','age','gender','animal','breed','color')

class EditDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('name','phone','qualification','email','password')

class EditServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('name','cost','time')

class EditPetserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Petservice
        fields = ('pserviceid','status')

class EditAdoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adoption
        fields = ('breed','animal','color','age','description','image','gender')

class EditBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('date','slot')

class EditHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = ('date','description','prescription')

class EditSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ('name','email','password')

class EditProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name','price','quantity','animal','producttype','rating','approved','productid')
        
class EditPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ('date','payed','delivery_status')

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('petid','name','age','gender','animal','breed','color')

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('serviceid','name','cost','time',)

class AdoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adoption
        fields = ('aid','breed','animal','color','age','description','image','gender','phone')

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('bid','slot','date','booking_type','booked_for','pet_id')

class AddBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('slot','date','booking_type','booked_for','pet_id','customer_id','doctor_id')

class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = ('hid','customer_id','pet_id','description','date','prescription')

class AddHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = ('customer_id','pet_id','description','date','prescription')

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ('sid','name','email','password')

class AddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('image','name','price','seller_id','quantity','animal','producttype','rating','approved')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('image','productid','name','price','quantity','animal','producttype','rating','approved')

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ('purchaseid','date','payed','delivery_status','product_id','customer_id')

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ('purchaseid','date','payed','delivery_status','product_id','customer_id')      

class PetServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Petservice
        fields = ('pserviceid','status','customer_id','pet_id','service_id')  

class CustomerChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields =('cid','password',)