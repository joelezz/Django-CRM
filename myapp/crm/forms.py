from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Customer


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

        username = forms.CharField(
            widget=forms.TextInput(attrs={
                'class': 'block w-full px-1 py-1 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
                'placeholder': 'Username'
            })
        )
        email = forms.EmailField(
            widget=forms.EmailInput(attrs={
                'class': 'block w-full px-1 py-1 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
                'placeholder': 'Email'
            })
        )
        password1 = forms.CharField(
            widget=forms.PasswordInput(attrs={
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
                'placeholder': 'Pwd'
            })
        )
        password2 = forms.CharField(
            widget=forms.PasswordInput(attrs={
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
                'placeholder': 'Confirm pwd'
            })
        )

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
            'placeholder': 'Enter your username...'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
            'placeholder': 'Enter your password...'
        })
    )

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

class AddCustomerForm(forms.ModelForm):
    class Meta:

        model = Customer
        fields = ('company', 'position', 'first_name', 'last_name', 'email', 'phone',)

        company = forms.CharField(
                widget=forms.TextInput(attrs={
                    'class': 'block w-full px-1 py-1 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
                })
            )
        position = forms.CharField(
                widget=forms.TextInput(attrs={
                    'class': 'block w-full px-1 py-1 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
                })
            )
        
        first_name = forms.CharField(
                widget=forms.TextInput(attrs={
                    'class': 'block w-full px-1 py-1 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
                })
            )
        
        last_name = forms.CharField(
                widget=forms.TextInput(attrs={
                    'class': 'block w-full px-1 py-1 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
                })
            )
        email = forms.CharField(
                widget=forms.TextInput(attrs={
                    'class': 'block w-full px-1 py-1 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
                })
            )
        phone = forms.CharField(
                widget=forms.TextInput(attrs={
                    'class': 'block w-full px-1 py-1 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
                })
            )
    