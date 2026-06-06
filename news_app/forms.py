from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from news_app.models import User_Profile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже существует')
        return email


class User_Update_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

    
class Profile_Update_Form(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = ('profile_image', 'phone', 'bio')
