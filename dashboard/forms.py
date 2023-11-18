from django import forms
from .models import Product, Staff 
from django.forms import ModelForm
from core.models import Service

class AddServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ('name', 'price', 'image')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class AddProductForm(forms.ModelForm):
    service = forms.ModelChoiceField(
        queryset=Service.objects.all().order_by('name'),
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Product
        fields = ('name', 'price', 'image', 'service')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

from django.contrib.auth.hashers import make_password 

class AddStaffForm(forms.ModelForm):
    service = forms.ModelChoiceField(
        queryset=Service.objects.all().order_by('name'),
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Staff
        fields = ('name', 'email', 'mobile', 'image', 'service', 'password')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),  # Use PasswordInput widget for password
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        staff = super().save(commit=False)
        staff.password = make_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            staff.save()
        return staff