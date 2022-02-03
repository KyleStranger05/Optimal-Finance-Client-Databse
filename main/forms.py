from django import forms
from .models import CompanyClass, IndividualClass
from django.forms import ModelForm

class CompanyForm(ModelForm):
    class Meta:
        model = CompanyClass
        fields = '__all__'
        widgets = {
            'FinancialYearEnd' : forms.SelectDateWidget,
            'ProvisionalTaxDate1' : forms.SelectDateWidget,
            'ProvisionalTaxDate2' : forms.SelectDateWidget,
            'ARMonth' : forms.SelectDateWidget,
        }

class CompanyIT14Form(ModelForm):
    class Meta:
        model = CompanyClass
        fields= ['isdone_IT14']

class IndividualForm(ModelForm):
    class Meta:
        model = IndividualClass
        fields = '__all__'
        widgets = {
            'ProvisionalTaxDate1': forms.SelectDateWidget,
            'ProvisionalTaxDate2': forms.SelectDateWidget,
        }
