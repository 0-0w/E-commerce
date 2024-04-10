from django import forms
from django.forms import ModelForm

from .models import SignUp

class SignUpForm(ModelForm):
    class Meta:
        model = SignUp
        fields = "__all__"
        # fields = ("username", "email", "password", "re_password")
        # path = forms.CharField(required=False)
        # name = forms.CharField()
        # email = forms.CharField(widget = forms.EmailField)
        password = forms.CharField(widget = forms.PasswordInput)
        re_password = forms.CharField(widget = forms.PasswordInput)

        # if password != re_password:
        #     raise forms.ValidationError("Password does not match")
            
