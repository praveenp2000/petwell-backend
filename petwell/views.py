from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
from rest_framework.utils import json
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.db.models import Sum
import json

from petwell.models import Customer,Pet,Admin,Product,Purchase,Doctor,Service,Petservice,Adoption,Booking,Health,Seller
from petwell.serializer import AddHealthSerializer,CustomerLoginSerializer,DoctorLoginSerializer,AdminLoginSerializer,SellerLoginSerializer,ServiceSerializer,AdoptionSerializer,BookingSerializer,HealthSerializer,PetServiceSerializer,SellerSerializer,ProductSerializer,PurchaseSerializer
from petwell.serializer import AddBookingSerializer,AddProductSerializer,CustomerSerializer,DoctorSerializer,AdminSerializer,SellerSerializer,EditCustomerSerializer,EditPetSerializer,EditDoctorSerializer,EditServiceSerializer,EditPetserviceSerializer,EditAdoptionSerializer,EditBookingSerializer,EditHealthSerializer,EditSellerSerializer,EditProductSerializer,EditPurchaseSerializer,PetSerializer

# Create your views here.

ALL_SLOTS = [
    "09:00 AM - 10:00 AM",
    "10:00 AM - 11:00 AM",
    "11:00 AM - 12:00 PM",
    "01:00 PM - 02:00 PM",
    "02:00 PM - 03:00 PM",
    "03:00 PM - 04:00 PM",
    "04:00 PM - 05:00 PM",
    "05:00 PM - 06:00 PM",
]

@csrf_exempt
def customerloginApi(request,id=0):
    if request.method=='POST':
        customer_data = JSONParser().parse(request)
        customerlogin_serializer = CustomerLoginSerializer(data=customer_data)
        if customerlogin_serializer.is_valid():
            if Customer.objects.filter(email=customer_data['email']).exists():
                customer = Customer.objects.get(email=customer_data['email'])
                if customer.password==customer_data['password']:
                    info = {
                        "cid": customer.cid,
                        "name": customer.name,
                        "email": customer.email,
                    }
                    return JsonResponse({"status": "success","message":"Login successfull","data":info},status=200,safe=False)
                else:
                    return JsonResponse({"status": "failed","message":"Wrong Password"},status=200,safe=False)
            else:
                return JsonResponse({"status": "failed","message":"Wrong Id"},status=200,safe=False)

@csrf_exempt
def doctorloginApi(request,id=0):
    if request.method=='POST':
        doctor_data = JSONParser().parse(request)
        doctorlogin_serializer = DoctorLoginSerializer(data=doctor_data)
        if doctorlogin_serializer.is_valid():
            if Doctor.objects.filter(email=doctor_data['email']).exists():
                doctor = Doctor.objects.get(email=doctor_data['email'])
                if doctor.password==doctor_data['password']:
                    info = {
                        "doctorid": doctor.doctorid,
                        "name": doctor.name,
                        "email": doctor.email,
                    }
                    return JsonResponse({"status": "success","message":"Login successfull","data":info},status=200,safe=False)
                else:
                    return JsonResponse({"status": "failed","message":"Wrong Password"},status=200,safe=False)
            else:
                return JsonResponse({"status": "failed","message":"Wrong Id"},status=200,safe=False)

@csrf_exempt
def adminloginApi(request,id=0):
    if request.method=='POST':
        admin_data = JSONParser().parse(request)
        adminlogin_serializer = AdminLoginSerializer(data=admin_data)
        if adminlogin_serializer.is_valid():
            if Admin.objects.filter(email=admin_data['email']).exists():
                admin = Admin.objects.get(email=admin_data['email'])
                if admin.password==admin_data['password']:
                    admin_info = {
                        "aid": admin.aid,
                        "name": admin.name,
                        "email": admin.email,
                    }
                    return JsonResponse({"status": "success","message":"Login successfull","data":admin_info},status=200,safe=False)
                else:
                    return JsonResponse({"status": "failed","message":"Wrong Password"},status=200,safe=False)
            else:
                return JsonResponse({"status": "failed","message":"Wrong Id"},status=200,safe=False)

@csrf_exempt
def sellerloginApi(request,id=0):
    if request.method=='POST':
        seller_data = JSONParser().parse(request)
        sellerlogin_serializer = SellerLoginSerializer(data=seller_data)
        if sellerlogin_serializer.is_valid():
            if Seller.objects.filter(email=seller_data['email']).exists():
                seller = Seller.objects.get(email=seller_data['email'])
                if seller.password==seller_data['password']:
                    info = {
                        "sid": seller.sid,
                        "name": seller.name,
                        "email": seller.email,
                    }
                    return JsonResponse({"status": "success","message":"Login successfull", "data":info },status=200,safe=False)
                else:
                    return JsonResponse({"status": "failed","message":"Wrong Password"},status=200,safe=False)
            else:
                return JsonResponse({"status": "failed","message":"Wrong Id"},status=200,safe=False)
        else:  print('serializer not valid')

@csrf_exempt
def customerregisterApi(request,id=0):
    if request.method=='POST':
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializer(data=customer_data)
        if Customer.objects.filter(email=customer_data['email']).exists():
            return JsonResponse("Email already exists", safe=False)
        elif customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        else:
            return JsonResponse("Failed to add",safe=False)

@csrf_exempt
def doctorregisterApi(request,id=0):
    if request.method=='POST':
        doctor_data = JSONParser().parse(request)
        doctor_serializer = DoctorSerializer(data=doctor_data)
        if Doctor.objects.filter(email=doctor_data['email']).exists():
            return JsonResponse("Email already exists", safe=False)
        elif doctor_serializer.is_valid():
            doctor_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        else:
            return JsonResponse("Failed to add",safe=False)

@csrf_exempt
def adminregisterApi(request,id=0):
    if request.method=='POST':
        admin_data = JSONParser().parse(request)
        admin_serializer = AdminSerializer(data=admin_data)
        if Admin.objects.filter(email=admin_data['email']).exists():
            return JsonResponse("Email already exists", safe=False)
        elif admin_serializer.is_valid():
            admin_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        else:
            return JsonResponse("Failed to add",safe=False)

@csrf_exempt
def sellerregisterApi(request,id=0):
    if request.method=='POST':
        seller_data = JSONParser().parse(request)
        seller_serializer = SellerSerializer(data=seller_data)
        if Seller.objects.filter(email=seller_data['email']).exists():
            return JsonResponse("Email already exists", safe=False)
        elif seller_serializer.is_valid():
            seller_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        else:
            return JsonResponse("Failed to add",safe=False)


@csrf_exempt
def addProductApi(request,id=0):
    if request.method=='POST':
        serializer = AddProductSerializer(data={
            "seller_id":request.POST.get("seller_id"),
            "name":request.POST.get("name"),
            "price":request.POST.get("price"),
            "quantity":request.POST.get("quantity"),
            "animal":request.POST.get("animal"),
            "producttype":request.POST.get("producttype"),
            "rating":request.POST.get("rating"),
            "approved":request.POST.get("approved"),
            "image":request.FILES.get("image"),
        })
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Added successfully", safe=False)

@csrf_exempt
def getAllPurchasesOfSellerApi(request, seller_id):
    purchase_count = Purchase.objects.filter(product_id__seller_id=seller_id).count()
    customer_count = Purchase.objects.filter(product_id__seller_id=seller_id).values('customer_id').distinct().count()
    total_revenue = Purchase.objects.filter(product_id__seller_id=seller_id, payed=True).aggregate(revenue=Sum('product_id__price'))['revenue']
    return JsonResponse({
        "seller_id": seller_id,
        "total_purchases": purchase_count,
        "total_customers": customer_count,
        "total_revenue": total_revenue
    })


@csrf_exempt
def editcustomerApi(request,id=0):
    if request.method=='PUT':
        customer_data = JSONParser().parse(request)
        customer= Customer.objects.get(cid=customer_data['cid'])
        customer_serializer = EditCustomerSerializer(customer,data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse("Update successfully", safe=False)
        else:
            return JsonResponse("Failed to Update",safe=False)


@csrf_exempt
def editpetApi(request,id=0):
    if request.method=='PUT':
        pet_data = JSONParser().parse(request)
        pet= Pet.objects.get(petid=pet_data['petid'])
        pet_serializer = EditPetSerializer(pet,data=pet_data)
        if pet_serializer.is_valid():
            pet_serializer.save()
            return JsonResponse("Update successfully", safe=False)
        else:
            return JsonResponse("Failed to Update",safe=False)


@csrf_exempt
def editdoctorApi(request,id=0):
    if request.method=='PUT':
        doctor_data = JSONParser().parse(request)
        doctor= Doctor.objects.get(doctorid=doctor_data['doctorid'])
        doctor_serializer = EditDoctorSerializer(doctor,data=doctor_data)
        if doctor_serializer.is_valid():
            doctor_serializer.save()
            return JsonResponse("Update successfully", safe=False)
        else:
            return JsonResponse("Failed to Update",safe=False)


@csrf_exempt
def editserviceApi(request,id=0):
    if request.method=='PUT':
        service_data = JSONParser().parse(request)
        service = Service.objects.get(serviceid=service_data['serviceid'])
        service_serializer = EditServiceSerializer(service,data=service_data)
        if service_serializer.is_valid():
            service_serializer.save()
            return JsonResponse("Update successfully", safe=False)
        else:
            return JsonResponse("Failed to Update",safe=False)

@csrf_exempt
def editpetserviceApi(request,id=0):
    if request.method=='PUT':
        petservice_data = JSONParser().parse(request)
        petservice = Petservice.objects.get(pserviceid=petservice_data['pserviceid'])
        petservice_serializer = EditPetserviceSerializer(petservice,data=petservice_data)
        if petservice_serializer.is_valid():
            petservice_serializer.save()
            return JsonResponse("Update successfully", safe=False)
        else:
            return JsonResponse("Failed to Update",safe=False)

@csrf_exempt
def editadoptionApi(request,id=0):
    if request.method=='PUT':
        adoption_data = JSONParser().parse(request)
        adoption = Adoption.objects.get(aid=adoption_data['aid'])
        adoption_serializer = EditAdoptionSerializer(adoption,data=adoption_data)
        if adoption_serializer.is_valid():
            adoption_serializer.save()
            return JsonResponse("Update successfully", safe=False)
        else:
            return JsonResponse("Failed to Update",safe=False)


@csrf_exempt
def addbookingApi(request,id=0):
    if request.method=='POST':
        b_data = JSONParser().parse(request)
        b_serializer = AddBookingSerializer(data=b_data)
        if b_serializer.is_valid():
            b_serializer.save()
            if b_serializer.save():
                return JsonResponse("Added successfully", safe=False)
        else:
            return JsonResponse("Not a valid serializer",safe=False)



@csrf_exempt
def addhealthApi(request,id=0):
    if request.method=='POST':
        b_data = JSONParser().parse(request)
        b_serializer = AddHealthSerializer(data=b_data)
        if b_serializer.is_valid():
            b_serializer.save()
            if b_serializer.save():
                return JsonResponse("Added successfully", safe=False)
        else:
            return JsonResponse("Not a valid serializer",safe=False)


@csrf_exempt
def getAvailableSlots(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            date = data.get("date")  
            booking_type = data.get("booking_type")
            if not date or not booking_type:
                return JsonResponse({"error": "Date is required"}, status=400)
            booked_slots = Booking.objects.filter(date=date, booking_type=booking_type).values_list("slot", flat=True)
            available_slots = [slot for slot in ALL_SLOTS if slot not in booked_slots]
            return JsonResponse({"date": date, "available_slots": available_slots}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

@csrf_exempt
def editbookingApi(request,id=0):
    if request.method=='PUT':
        booking_data = JSONParser().parse(request)
        booking = Booking.objects.get(bid=booking_data['bid'])
        booking_serializer = EditBookingSerializer(booking,data=booking_data)
        if booking_serializer.is_valid():
            booking_serializer.save()
            return JsonResponse("Update successfully", safe=False)
        else:
            return JsonResponse("Failed to Update",safe=False)

@csrf_exempt
def getbookingbyidApi(request,id=0):
    if request.method=='GET':
        booking = Booking.objects.get(bid=id)
        booking_serializer = BookingSerializer(booking)
        return JsonResponse(booking_serializer.data, safe=False) 


@csrf_exempt
def getallbookingApi(request,id=0):
        data = json.loads(request.body)
        current_page = int(data.get("current_page", 1))  # Default to page 1
        page_size = int(data.get("page_size", 10))  # Default to 10 items per page
        customer_id = data.get("customer_id", None)  # Get customer_id if provided

        # Filter bookings by customer_id if provided
        if customer_id:
            bookings = Booking.objects.filter(customer_id=customer_id)
        else:
            bookings = Booking.objects.all()

        total_records = bookings.count()

        # Apply pagination
        paginator = Paginator(bookings, page_size)
        paginated_data = paginator.get_page(current_page)

        # Serialize paginated customer data
        booking_serializer = BookingSerializer(paginated_data, many=True)

        return JsonResponse({
            "data": booking_serializer.data,  # Customer records
            "total_records": total_records,  # Total customer count
            "page_size": page_size,  # Number of items per page
            "current_page": current_page  # Current requested page
        }, safe=False)



@csrf_exempt
def getallbookingbyDocIdAndDateApi(request,id=0):
        data = json.loads(request.body)
        doctor_id = int(data.get("doctor_id")) 
        date = data.get("date", None)  

        if doctor_id:
            bookings = Booking.objects.filter(doctor_id=doctor_id, date=date)
            booking_serializer = BookingSerializer(bookings, many=True)
            return JsonResponse({
                "data": booking_serializer.data, 
            }, safe=False)



@csrf_exempt
def getBookingByDoctorIdApi(request,id=0):
    if request.method=='GET':
        booking = Booking.objects.filter(doctor_id=id)
        booking_serializer = BookingSerializer(booking,many=True)
        return JsonResponse(booking_serializer.data, safe=False) 


@csrf_exempt
def edithealthApi(request,id=0):
    if request.method=='PUT':
        health_data = JSONParser().parse(request)
        health = Health.objects.get(hid=health_data['hid'])
        health_serializer = EditHealthSerializer(health,data=health_data)
        if health_serializer.is_valid():
            health_serializer.save()
            return JsonResponse("Update successfully", safe=False)
        else:
            return JsonResponse("Failed to Update",safe=False)

@csrf_exempt
def editserviceApi(request,id=0):
    if request.method=='PUT':
        service_data = JSONParser().parse(request)
        service = Service.objects.get(serviceid=service_data['serviceid'])
        service_serializer = EditServiceSerializer(service,data=service_data)
        if service_serializer.is_valid():
            service_serializer.save()
            return JsonResponse("Update successfully", safe=False)
        else:
            return JsonResponse("Failed to Update",safe=False)

@csrf_exempt
def editsellerApi(request,id=0):
    if request.method=='PUT':
        seller_data = JSONParser().parse(request)
        seller = Seller.objects.get(sid=seller_data['sid'])
        seller_serializer = EditSellerSerializer(seller,data=seller_data)
        if seller_serializer.is_valid():
            seller_serializer.save()
            return JsonResponse("Update successfully", safe=False)
        else:
            return JsonResponse("Failed to Update",safe=False)

@csrf_exempt
def editproductApi(request,id=0):
    if request.method=='PUT':
        product_data = JSONParser().parse(request)
        product = Product.objects.get(productid=product_data['productid'])
        product_serializer = EditProductSerializer(product,data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Update successfully", safe=False)
        else:
            return JsonResponse("Failed to Update",safe=False)

@csrf_exempt
def editpurchaseApi(request,id=0):
    if request.method=='PUT':
        purchase_data = JSONParser().parse(request)
        purchase = Purchase.objects.get(purchaseid=purchase_data['purchaseid'])
        purchase_serializer = EditPurchaseSerializer(purchase,data=purchase_data)
        if purchase_serializer.is_valid():
            purchase_serializer.save()
            return JsonResponse("Update successfully", safe=False)
        else:
            return JsonResponse("Failed to Update",safe=False)

@csrf_exempt
def getcustomerbyidApi(request,id=0):
    if request.method=='GET':
        customer = Customer.objects.get(cid=id)
        customer_serializer = CustomerSerializer(customer)
        return JsonResponse(customer_serializer.data, safe=False) 


@csrf_exempt
def getallcustomerApi(request,id=0):
        data = json.loads(request.body)
        current_page = int(data.get("current_page", 1))  # Default to page 1
        page_size = int(data.get("page_size", 10))  # Default to 10 items per page

        # Fetch all customer records
        customers = Customer.objects.all()
        total_records = customers.count()

        # Apply pagination
        paginator = Paginator(customers, page_size)
        paginated_data = paginator.get_page(current_page)

        # Serialize paginated customer data
        customer_serializer = CustomerSerializer(paginated_data, many=True)

        return JsonResponse({
            "data": customer_serializer.data,  # Customer records
            "total_records": total_records,  # Total customer count
            "page_size": page_size,  # Number of items per page
            "current_page": current_page  # Current requested page
        }, safe=False)

@csrf_exempt
def getdoctorbyidApi(request,id=0):
    if request.method=='GET':
        doctor = Doctor.objects.get(doctorid=id)
        doctor_serializer = DoctorSerializer(doctor)
        return JsonResponse(doctor_serializer.data, safe=False) 


@csrf_exempt
def getpetservicebyidApi(request,id=0):
    if request.method=='GET':
        petservice = Petservice.objects.get(pserviceid=id)
        petservice_serializer = PetServiceSerializer(petservice)
        return JsonResponse(petservice_serializer.data, safe=False) 


@csrf_exempt
def getallpetserviceApi(request,id=0):
        data = json.loads(request.body)
        current_page = int(data.get("current_page", 1))  # Default to page 1
        page_size = int(data.get("page_size", 10))  # Default to 10 items per page

        # Fetch all customer records
        petservice = Petservice.objects.all()
        total_records = petservice.count()

        # Apply pagination
        paginator = Paginator(petservice, page_size)
        paginated_data = paginator.get_page(current_page)

        # Serialize paginated customer data
        petservice_serializer = PetServiceSerializer(paginated_data, many=True)

        return JsonResponse({
            "data": petservice_serializer.data,  # Customer records
            "total_records": total_records,  # Total customer count
            "page_size": page_size,  # Number of items per page
            "current_page": current_page  # Current requested page
        }, safe=False)

@csrf_exempt
def getservicebyidApi(request,id=0):
    if request.method=='GET':
        service = Service.objects.get(serviceid=id)
        service_serializer = ServiceSerializer(service)
        return JsonResponse(service_serializer.data, safe=False) 


@csrf_exempt
def getallserviceApi(request,id=0):
        data = json.loads(request.body)
        current_page = int(data.get("current_page", 1))  # Default to page 1
        page_size = int(data.get("page_size", 10))  # Default to 10 items per page

        # Fetch all customer records
        service = Service.objects.all()
        total_records = pet.count()

        # Apply pagination
        paginator = Paginator(service, page_size)
        paginated_data = paginator.get_page(current_page)

        # Serialize paginated customer data
        service_serializer = ServiceSerializer(paginated_data, many=True)

        return JsonResponse({
            "data": service_serializer.data,  # Customer records
            "total_records": total_records,  # Total customer count
            "page_size": page_size,  # Number of items per page
            "current_page": current_page  # Current requested page
        }, safe=False)

@csrf_exempt
def getadoptionbyidApi(request,id=0):
    if request.method=='GET':
        adoption = Adoption.objects.get(aid=id)
        adoption_serializer = AdoptionSerializer(adoption)
        return JsonResponse(adoption_serializer.data, safe=False) 


@csrf_exempt
def getalladoptionApi(request,id=0):
        data = json.loads(request.body)
        current_page = int(data.get("current_page", 1))  # Default to page 1
        page_size = int(data.get("page_size", 10))  # Default to 10 items per page

        # Fetch all customer records
        adoption = Adoption.objects.all()
        total_records = adoption.count()

        # Apply pagination
        paginator = Paginator(adoption, page_size)
        paginated_data = paginator.get_page(current_page)

        # Serialize paginated customer data
        adoption_serializer = AdoptionSerializer(paginated_data, many=True)

        return JsonResponse({
            "data": adoption_serializer.data,  # Customer records
            "total_records": total_records,  # Total customer count
            "page_size": page_size,  # Number of items per page
            "current_page": current_page  # Current requested page
        }, safe=False)

@csrf_exempt
def gethealthbyidApi(request,id=0):
    if request.method=='GET':
        health = Health.objects.get(hid=id)
        health_serializer = HealthSerializer(pet)
        return JsonResponse(health_serializer.data, safe=False) 


@csrf_exempt
def getallhealthApi(request,id=0):
        data = json.loads(request.body)
        current_page = int(data.get("current_page", 1))  # Default to page 1
        page_size = int(data.get("page_size", 10))  # Default to 10 items per page

        # Fetch all customer records
        health = Health.objects.all()
        total_records = health.count()

        # Apply pagination
        paginator = Paginator(health, page_size)
        paginated_data = paginator.get_page(current_page)

        # Serialize paginated customer data
        health_serializer = HealthSerializer(paginated_data, many=True)

        return JsonResponse({
            "data": health_serializer.data,  # Customer records
            "total_records": total_records,  # Total customer count
            "page_size": page_size,  # Number of items per page
            "current_page": current_page  # Current requested page
        }, safe=False)

@csrf_exempt
def getsellerbyidApi(request,id=0):
    if request.method=='GET':
        seller = Seller.objects.get(sid=id)
        seller_serializer = SellerSerializer(seller)
        return JsonResponse(seller_serializer.data, safe=False) 


@csrf_exempt
def getallsellerApi(request,id=0):
        data = json.loads(request.body)
        current_page = int(data.get("current_page", 1))  # Default to page 1
        page_size = int(data.get("page_size", 10))  # Default to 10 items per page

        # Fetch all customer records
        seller = Seller.objects.all()
        total_records = seller.count()

        # Apply pagination
        paginator = Paginator(seller, page_size)
        paginated_data = paginator.get_page(current_page)

        # Serialize paginated customer data
        seller_serializer = SellerSerializer(paginated_data, many=True)

        return JsonResponse({
            "data": seller_serializer.data,  # Customer records
            "total_records": total_records,  # Total customer count
            "page_size": page_size,  # Number of items per page
            "current_page": current_page  # Current requested page
        }, safe=False)

@csrf_exempt
def getproductbyidApi(request,id=0):
    if request.method=='GET':
        product = Product.objects.get(productid=id)
        product_serializer = ProductSerializer(product)
        return JsonResponse(product_serializer.data, safe=False)

@csrf_exempt
def getproductbysellerApi(request,id=0):
    data = json.loads(request.body)
    current_page = int(data.get("current_page", 1))  # Default to page 1
    page_size = int(data.get("page_size", 10))  # Default to 10 items per page

    # Fetch all customer records
    product = Product.objects.filter(seller_id=id)
    total_records = product.count()

    # Apply pagination
    paginator = Paginator(product, page_size)
    paginated_data = paginator.get_page(current_page)

    # Serialize paginated customer data
    product_serializer = ProductSerializer(paginated_data, many=True)

    return JsonResponse({
        "data": product_serializer.data,  # Customer records
        "total_records": total_records,  # Total customer count
        "page_size": page_size,  # Number of items per page
        "current_page": current_page  # Current requested page
    }, safe=False)
 


@csrf_exempt
def getallproductApi(request,id=0):
        data = json.loads(request.body)
        current_page = int(data.get("current_page", 1))  # Default to page 1
        page_size = int(data.get("page_size", 10))  # Default to 10 items per page

        # Fetch all customer records
        product = Product.objects.all().order_by('approved')
        total_records = product.count()

        # Apply pagination
        paginator = Paginator(product, page_size)
        paginated_data = paginator.get_page(current_page)

        # Serialize paginated customer data
        product_serializer = ProductSerializer(paginated_data, many=True)

        return JsonResponse({
            "data": product_serializer.data,  # Customer records
            "total_records": total_records,  # Total customer count
            "page_size": page_size,  # Number of items per page
            "current_page": current_page  # Current requested page
        }, safe=False)


@csrf_exempt
def getapprovedproductApi(request,id=0):
        data = json.loads(request.body)
        current_page = int(data.get("current_page", 1))  # Default to page 1
        page_size = int(data.get("page_size", 10))  # Default to 10 items per page

        # Fetch all customer records
        product = Product.objects.all().filter(approved=True)
        total_records = product.count()

        # Apply pagination
        paginator = Paginator(product, page_size)
        paginated_data = paginator.get_page(current_page)

        # Serialize paginated customer data
        product_serializer = ProductSerializer(paginated_data, many=True)

        return JsonResponse({
            "data": product_serializer.data,  # Customer records
            "total_records": total_records,  # Total customer count
            "page_size": page_size,  # Number of items per page
            "current_page": current_page  # Current requested page
        }, safe=False)




@csrf_exempt
def getpurchasebyidApi(request,id=0):
    if request.method=='GET':
        purchase = Purchase.objects.get(purchaseid=id)
        purchase_serializer = PurchaseSerializer(purchase)
        return JsonResponse(purchase_serializer.data, safe=False)


@csrf_exempt
def getallpurchaseApi(request,id=0):
        data = json.loads(request.body)
        current_page = int(data.get("current_page", 1))  # Default to page 1
        page_size = int(data.get("page_size", 10))  # Default to 10 items per page

        # Fetch all customer records
        purchase = Purchase.objects.all()
        total_records = purchase.count()

        # Apply pagination
        paginator = Paginator(purchase, page_size)
        paginated_data = paginator.get_page(current_page)

        # Serialize paginated customer data
        purchase_serializer = PurchaseSerializer(paginated_data, many=True)

        return JsonResponse({
            "data": purchase_serializer.data,  # Customer records
            "total_records": total_records,  # Total customer count
            "page_size": page_size,  # Number of items per page
            "current_page": current_page  # Current requested page
        }, safe=False)

@csrf_exempt
def getpetbyidApi(request,id=0):
    if request.method=='GET':
        pet = Pet.objects.get(petid=id)
        pet_serializer = PetSerializer(pet)
        return JsonResponse(pet_serializer.data, safe=False)

@csrf_exempt
def getcustomerIdFromPetId(request,id=0):
    if request.method=='GET':
        pet = Pet.objects.get(petid=id)  # Ensure petid is the correct field name
        cid = pet.customer_id.cid
        return JsonResponse({"cid": cid}, safe=False)


@csrf_exempt
def getcustomerpetsApi(request,id=0):
    if request.method=='GET':
        pet = Pet.objects.filter(customer_id=id)
        pet_serializer = PetSerializer(pet, many=True)
        return JsonResponse(pet_serializer.data, safe=False) 

@csrf_exempt
def getallpetApi(request,id=0):
        data = json.loads(request.body)
        current_page = int(data.get("current_page", 1))  # Default to page 1
        page_size = int(data.get("page_size", 10))  # Default to 10 items per page

        # Fetch all customer records
        pet = Pet.objects.all()
        total_records = pet.count()

        # Apply pagination
        paginator = Paginator(pet, page_size)
        paginated_data = paginator.get_page(current_page)

        # Serialize paginated customer data
        pet_serializer = PetSerializer(paginated_data, many=True)

        return JsonResponse({
            "data": pet_serializer.data,  # Customer records
            "total_records": total_records,  # Total customer count
            "page_size": page_size,  # Number of items per page
            "current_page": current_page  # Current requested page
        }, safe=False)

@csrf_exempt
def getservicebyidApi(request,id=0):
    if request.method=='GET':
        service = Service.objects.get(serviceid=id)
        service_serializer = ServiceSerializer(service)
        return JsonResponse(service_serializer.data, safe=False) 


@csrf_exempt
def getallserviceApi(request,id=0):
        data = json.loads(request.body)
        current_page = int(data.get("current_page", 1))  # Default to page 1
        page_size = int(data.get("page_size", 10))  # Default to 10 items per page

        # Fetch all customer records
        service = Service.objects.all()
        total_records = service.count()

        # Apply pagination
        paginator = Paginator(service, page_size)
        paginated_data = paginator.get_page(current_page)

        # Serialize paginated customer data
        service_serializer = ServiceSerializer(paginated_data, many=True)

        return JsonResponse({
            "data": service_serializer.data,  # Customer records
            "total_records": total_records,  # Total customer count
            "page_size": page_size,  # Number of items per page
            "current_page": current_page  # Current requested page
        }, safe=False)

