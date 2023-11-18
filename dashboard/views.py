from django.shortcuts import render, redirect
from core.models import Customer, Service, Appointment
from .models import Product, Staff 
from .forms import AddServiceForm
from .forms import AddProductForm
from .forms import AddStaffForm
from django.contrib.auth import logout



# Create your views here.
def home(request):
    count_services = Service.get_services_count()
    count_products = Product.get_products_count()
    count_staffs = Staff.get_staffs_count()
    count_customers = Customer.get_customers_count()
    count_appoint = Appointment.get_appoint_count()
    return render(request, 'dashboard/home.html', {'count_services': count_services, 'count_products': count_products, 'count_staffs': count_staffs, 'count_customers': count_customers, 'count_appoint': count_appoint})

def add_services(request):
    form = AddServiceForm
    if request.method == 'POST':
        form = AddServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = AddServiceForm
    return render(request, 'dashboard/add_services.html', {'form': form}) 

def addProducts(request):
    form = AddProductForm
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = AddProductForm
    return render(request, 'dashboard/addProducts.html', {'form': form})

def addStaffs(request):
    form = AddStaffForm
    if request.method == 'POST':
        form = AddStaffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = AddStaffForm
    return render(request, 'dashboard/addstaffs.html', {'form': form})   



def edit_service(request, id):
    form = AddServiceForm
    if request.method == 'POST':
        service = Service.objects.get(pk=id)
        form = AddServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('all_services')
    else:
        service = Service.objects.get(pk=id)
        form = AddServiceForm(instance=service)
    return render(request, 'dashboard/edit_service.html', {'form': form})

def editProduct(request, id):
    form = AddProductForm
    if request.method == 'POST':
        product = Product.objects.get(pk=id)
        form = AddProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('all_products')
    else:
        product = Product.objects.get(pk=id)
        form = AddProductForm(instance=product)
    return render(request, 'dashboard/editProduct.html', {'form': form})

def editStaff(request, id):
    form = AddStaffForm
    if request.method == 'POST':
        staff = Staff.objects.get(pk=id)
        form = AddStaffForm(request.POST, request.FILES, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('all_staffs')
    else:
        staff = Staff.objects.get(pk=id)
        form = AddStaffForm(instance=staff)
    return render(request, 'dashboard/editStaff.html', {'form': form})


def delete_service(request, id):
    if request.method == 'POST':
        service = Service.objects.get(pk=id)
        service.delete()
        return redirect('all_services')
    

def deleteProduct(request, id):
    if request.method == 'POST':
        product = Product.objects.get(pk=id)
        product.delete()
        return redirect('all_products')

def deleteStaff(request, id):
    if request.method == 'POST':
        staff = Staff.objects.get(pk=id)
        staff.delete()
        return redirect('all_staffs')

from django.db.models import Q

def all_services(request):
    search_name_query = request.GET.get('search_name', '')
    if search_name_query:
        services = Service.objects.filter(name__icontains=search_name_query)
    else:
        services = Service.get_all_services()
    return render(request, 'dashboard/all_services.html', {'services': services, 'search_name_query': search_name_query})

def all_products(request):
    search_name_query = request.GET.get('search_name', '')
    search_service_query = request.GET.get('search_service', '')
    
    if search_name_query or search_service_query:
        products = Product.objects.filter(
            Q(name__icontains=search_name_query) | 
            Q(service__name__icontains=search_service_query)
        )
    else:
        products = Product.get_all_products()

    return render(request, 'dashboard/all_products.html', {'products': products, 'search_name_query': search_name_query, 'search_service_query': search_service_query})


def all_staffs(request):
    search_name_query = request.GET.get('search_name', '')
    search_service_query = request.GET.get('search_service', '')
    
    if search_name_query or search_service_query:
        staffs = Staff.objects.filter(
            Q(name__icontains=search_name_query) | 
            Q(service__name__icontains=search_service_query)
        )
    else:
        staffs = Staff.get_all_staffs()

    return render(request, 'dashboard/all_staffs.html', {'staffs': staffs, 'search_name_query': search_name_query, 'search_service_query': search_service_query})


from datetime import datetime
def all_appointment(request):
    search_name_query = request.GET.get('search_name')
    search_date_query = request.GET.get('search_date')

    # Convert the date string to a datetime object
    if search_date_query:
        try:
            search_date_query = datetime.strptime(search_date_query, "%Y-%m-%d").date()
        except ValueError:
            search_date_query = None

    # Filter appointments based on search parameters
    appointments = Appointment.objects.all()

    if search_name_query:
        appointments = appointments.filter(your_name__icontains=search_name_query)

    if search_date_query:
        appointments = appointments.filter(your_date=search_date_query)

    return render(request, 'dashboard/all_appointment.html', {
        'appointments': appointments,
        'search_name_query': search_name_query,
        'search_date_query': request.GET.get('search_date'),  # Pass the original query for repopulating the form
    })



def all_customers(request):
    search_name_query = request.GET.get('search_name', '')
    search_email_query = request.GET.get('search_email', '')
    if search_name_query or search_email_query:
        customers = Customer.objects.filter(Q(first_name__icontains=search_name_query) | Q(email__icontains=search_email_query))
    else:
        customers = Customer.get_all_customers()
    return render(request, 'dashboard/all_customers.html', {'customers': customers, 'search_name_query': search_name_query, 'search_email_query': search_email_query})

def logoutAdmin(request):
    logout(request)
    return redirect('admin_login')
       