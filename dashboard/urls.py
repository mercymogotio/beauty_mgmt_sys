from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('add_services/', views.add_services, name='add_services'),
   path('addProducts/', views.addProducts, name='addProducts'),
   path('addStaffs/', views.addStaffs, name='addStaffs'),
   path('edit_service/<int:id>/', views.edit_service, name='edit_service'),
   path('editProduct/<int:id>/', views.editProduct, name='editProduct'),
   path('editStaff/<int:id>/', views.editStaff, name='editStaff'),
   path('delete_service/<int:id>/', views.delete_service, name='delete_service'),
   path('deleteProduct/<int:id>/', views.deleteProduct, name='deleteProduct'),
   path('deleteStaff/<int:id>/', views.deleteStaff, name='deleteStaff'),
   path('all_services/', views.all_services, name='all_services'),
   path('all_products/', views.all_products, name='all_products'),
   path('all_staffs/', views.all_staffs, name='all_staffs'),
   path('all_customers/', views.all_customers, name='all_customers'),
   path('all_appointment/', views.all_appointment, name='all_appointment'),
   path('logout/', views.logoutAdmin, name='logout'),
]