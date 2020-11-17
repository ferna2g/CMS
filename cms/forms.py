from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(required=True, min_length=4, max_length=50)
    email = forms.EmailField(required=True, min_length=4, max_length=50)
    password = forms.CharField(required=True, min_length=4, max_length=50)
