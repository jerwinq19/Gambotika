from django.contrib.auth.models import User
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label="username"
    )
    password = forms.CharField(
        label="password",
        widget=forms.PasswordInput()
    )
    
    
class RegisterForm(forms.ModelForm):
    re_enter_password = forms.CharField(
        label="Re-type Password:",
        widget=forms.PasswordInput()
    )
    
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]
        widgets = {
            'password': forms.PasswordInput()
        }
        
    def clean(self):
        clean_data = super().clean()
        
        password = clean_data.get('password')
        re_enter_password = clean_data.get('re_enter_password')
        
        if password != re_enter_password:
            raise forms.ValidationError('Password does not match...')
        
        return clean_data