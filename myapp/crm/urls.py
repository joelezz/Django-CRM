from django.urls import path
from . import views
from .views import upload_csv
from .views import export_customers_csv


urlpatterns = [
    path('register', views.register, name="register"),
    path('my-login', views.my_login, name="my-login"),
    path('customers', views.customers, name="customers"),
    path('record/<int:pk>/', views.record, name="record"),
    path('delete_record/<int:pk>', views.delete_record, name="delete_record"),
    path('update_record/<int:pk>', views.update_record, name="update_record"),
    path('add_customer', views.add_customer, name="add_customer"),
    path('logout', views.logout, name="logout"),
    path('upload_csv/', upload_csv, name='upload_csv'),
    path('export_customers_csv/', export_customers_csv, name='export_customers_csv'),

]