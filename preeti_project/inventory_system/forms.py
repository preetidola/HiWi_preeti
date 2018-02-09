from django import forms

class Login(forms.Form):
    uid = forms.EmailField(error_messages={'required':'Please enter your valid email address'},label='Email',max_length=100)
    pwd = forms.CharField(label='Password', max_length=40, widget=forms.PasswordInput())
