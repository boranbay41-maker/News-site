from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from news_app.models import User_Profile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput,
        help_text="Пароль должен содержать минимум 8 символов"
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput,
        help_text="Введите пароль еще раз"
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже существует')
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2


class User_Update_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

    
class Profile_Update_Form(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = ('profile_image', 'phone', 'bio')
