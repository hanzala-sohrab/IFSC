from django import forms


class BankForm(forms.Form):
    ifs_code = forms.CharField(max_length=15, required=False)
    bank_name = forms.CharField(max_length=100, required=False)
    city_name = forms.CharField(max_length=50, required=False)
