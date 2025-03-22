from django.urls import path,re_path
from petwell import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('customerlogin/',views.customerloginApi),
    path('doctorlogin/',views.doctorloginApi),
    path('adminlogin/',views.adminloginApi),
    path('sellerlogin/',views.sellerloginApi),


    path('customerregister/',views.customerregisterApi),
    path('doctorregister/',views.doctorregisterApi),
    path('adminregister/',views.adminregisterApi),
    path('sellerregister/',views.sellerregisterApi),


    path('editcustomer/',views.editcustomerApi),
    path('getallcustomer/',views.getallcustomerApi),
    re_path('getcustomerbyid/([0-9]+)$',views.getcustomerbyidApi),


    # path('addpet/',views.addpetApi),
    path('editpet/',views.editpetApi), 
    path('getallpet/',views.getallpetApi),
    re_path('getpetbyid/([0-9]+)$',views.getpetbyidApi),


    path('editdoctor/',views.editdoctorApi), 
    re_path('getdoctorbyid/([0-9]+)$',views.getdoctorbyidApi),


    # path('addservice/',views.addserviceApi),
    path('editservice/',views.editserviceApi), 
    path('getallservice/',views.getallserviceApi),
    re_path('getservicebyid/([0-9]+)$',views.getservicebyidApi),





    # path('addpetservice/',views.addpetserviceApi),
    path('editpetservice/',views.editpetserviceApi), 
    path('getallpetservice/',views.getallpetserviceApi),
    re_path('getpetservicebyid/([0-9]+)$',views.getpetservicebyidApi),


    # path('addadoption/',views.addadoptionApi),
    path('editadoption/',views.editadoptionApi), 
    path('getalladoption/',views.getalladoptionApi),
    re_path('getadoptionbyid/([0-9]+)$',views.getadoptionbyidApi),


    # path('addbooking/',views.addbookingApi),
    path('editbooking/',views.editbookingApi), 
    path('getallbooking/',views.getallbookingApi),
    re_path('getbookingbyid/([0-9]+)$',views.getbookingbyidApi),

    
    # path('addhealth/',views.addhealthApi),
    path('edithealth/',views.edithealthApi), 
    path('getallhealth/',views.getallhealthApi),
    re_path('gethealthbyid/([0-9]+)$',views.gethealthbyidApi),


    # path('addseller/',views.addsellerApi),
    path('editseller/',views.editsellerApi), 
    path('getallseller/',views.getallsellerApi),
    re_path('getsellerbyid/([0-9]+)$',views.getsellerbyidApi),
    re_path('getallpurchasesofseller/([0-9]+)$',views.getAllPurchasesOfSellerApi),


    path('addproduct/',views.addProductApi),
    path('editproduct/',views.editproductApi), 
    path('getallproduct/',views.getallproductApi),
    re_path('getproductbyid/([0-9]+)$',views.getproductbyidApi),
    re_path('getproductbysellerid/([0-9]+)$',views.getproductbysellerApi),


    # path('addpurchase/',views.addpurchaseApi),
    path('editpurchase/',views.editpurchaseApi), 
    path('getallpurchase/',views.getallpurchaseApi),
    re_path('getpurchasebyid/([0-9]+)$',views.getpurchasebyidApi),
]