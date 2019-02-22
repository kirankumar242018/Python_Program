from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):  # gives the information of the custom user creation form
        model = CustomUser  # takes the model of Custom User
        fields = ('username', 'email')  # fields of a class


class CustomUserChangeForm(UserChangeForm):
    class Meta:  # gives the information of the custom user change form
        model = CustomUser  # takes the model of Custom User
        fields = UserChangeForm.Meta.fields  # fields of a class User change form


class UserRegistrationForm(UserCreationForm):
    # email = forms.EmailField()  # takes email fields
    email = forms.RegexField(regex=r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
                             required=True)

    class Meta:  # gives the information of the user registration form
        model = User  # assigns model to user
        fields = ['username', 'email', 'password1', 'password2']  # fields of a class

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()

        return user


class LoginForm(forms.ModelForm):
    email = forms.EmailField()  # takes email fields

    class Meta:  # gives the information of the Login form
        model = User  # assigns model to user
        fields = ['username', 'password']  # fields of a class
