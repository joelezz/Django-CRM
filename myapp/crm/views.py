from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as logouts
from .forms import SignUpForm, LoginForm
from .models import Customer
import csv
from .forms import CsvImportForm, AddCustomerForm


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')  # Redirect to login page after successful signup
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def my_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page
                return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'my-login.html', {'form': form})

def upload_csv(request):
    if request.method == "POST":
        form = CsvImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                Customer.objects.create(
                    company=row['company'],
                    position=row['position'],
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    email=row['email'],
                    phone=row['phone']
                )
            return redirect('customers')  # Redirect to a customers page after import
    else:
        form = CsvImportForm()
    return render(request, 'upload_csv.html', {'form': form})

def export_customers_csv(request):
    customers = Customer.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="customers.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['company', 'position', 'first_name', 'last_name', 'email', 'phone'])

    for customer in customers:
        writer.writerow([customer.company, customer.position, customer.first_name, customer.last_name, customer.email, customer.phone])

    return response

def add_customer(request):
    if request.user.is_authenticated:
        customers = Customer.objects.all()
    if request.method == 'POST':
        form = AddCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New customer created")
            return render(request, 'customers.html', {'customers': customers}) 
    else:
        form = AddCustomerForm()
    return render(request, 'add_customer.html', {'form': form})

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Customer.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Customer deleted")
        return redirect('customers')
    else:
        messages.success(request, "You must be logged in to delete customers")
        return redirect('index')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Customer.objects.get(id=pk)
        form = AddCustomerForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated!")
            return redirect('customers')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "You must be logged in...")
        return redirect('index')

def customers(request):
    if request.user.is_authenticated:
        customers = Customer.objects.all()
    else:
        customers = None
    return render(request, 'customers.html', {'customers': customers} )

def record(request, pk):
    if request.user.is_authenticated:
        record = Customer.objects.get(id=pk)
        return render(request, 'record.html', {'record': record} )
    else:
        messages.success(request, "You must be logged in to see customer records")
        return redirect('home')

def logout(request):
    if request.method == 'POST':
        logouts(request)
        return redirect('')