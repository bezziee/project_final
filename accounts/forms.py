from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from .models import *


# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password1']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

class CreateEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['phoneNumber', 'salary']


class editEmployee(ModelForm):
    class Meta:
        model = Employee
        fields = ["phoneNumber", "salary"]


class editUser(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class editGuest(ModelForm):
    class Meta:
        model = Guest
        fields = ["phoneNumber"]


class ROLES(forms.Form):
    ROLES_TYPES = [
        ('manager', 'manager'),
        ('receptionist', 'receptionist'),
        ('staff', 'staff'),
    ]
    ROLES_TYPES = forms.CharField(
        widget=forms.RadioSelect(choices=ROLES_TYPES))
