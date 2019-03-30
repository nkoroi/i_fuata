from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .entities import *
from django.db import transaction
from django.utils.translation import ugettext_lazy as _


class FarmerCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Farmer
        fields = ('username', 'email')
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_farmer = True
        user.save()
        farmer = farmer.objects.create(user=user)
        farmer.email.add(*self.cleaned_data.get('email'))
        return user

class SalesOutletCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = SalesOutlet
        fields = ('username', 'email')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_sales = True
        user.save()
        sales = sales.objects.create(user=user)
        sales.email.add(*self.cleaned_data.get('email'))
        sales.username.add(*self.cleaned_data.get('username'))
        return user


class QA_LabCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = QA_Lab
        fields = ('username', 'email', 'license_no', 'license_exp_date', 'current_station_of_work')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_lab = True
        user.save()
        lab = lab.objects.create(user=user)
        lab.email.add(*self.cleaned_data.get('email'))
        lab.license_no.add(*self.cleaned_data.get('license_no'))
        lab.license_exp_date.add(*self.cleaned_data.get('license_exp_date'))
        lab.current_station_of_work.add(*self.cleaned_data.get('current_station_of_work'))
        return user



class VetMedicineDistributerCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = VetMedicineDistributer
        fields = ('username', 'email', 'license_no', 'license_exp_date', 'current_station_of_work')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_vmd = True
        user.save()
        vmd = vmd.objects.create(user=user)
        vmd.email.add(*self.cleaned_data.get('email'))
        vmd.license_no.add(*self.cleaned_data.get('license_no'))
        vmd.license_exp_date.add(*self.cleaned_data.get('license_exp_date'))
        vmd.current_station_of_work.add(*self.cleaned_data.get('current_station_of_work'))
        return user
