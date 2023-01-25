from django import forms

class regform(forms.Form):
    name = forms.CharField(max_length=20)
    address = forms.CharField(max_length=200)
    gender = forms.CharField(max_length=20)
    state = forms.CharField(max_length=50)

