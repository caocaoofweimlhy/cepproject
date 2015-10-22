from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Hidden, Button, HTML, Div, Field, Row, Fieldset

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('address','age','website', 'picture', 'contact')

# class AccountForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = '__all__'
    
#     helper = FormHelper()
#     helper.form_method = 'POST'
#     helper.add_input(Submit('Save', 'Save', css_class='btn-primary'))
    