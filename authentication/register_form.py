from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    username = forms.CharField(
        label='Username',
        max_length=150,
        help_text='Необходимый. 150 символов или меньше. Только буквы, цифры и @/./+/-/_.',

        error_messages={'unique': "Пользователь с таким именем уже существует."},
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя ползователья'})
    )

    first_name = forms.CharField(
        max_length=12, 
        min_length=4, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'})
    )
    last_name = forms.CharField(
        max_length=12, 
        min_length=4, 
        required=True,
        widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}))
    )
    email = forms.EmailField(
        max_length=50, 
        help_text='Необходимый. Сообщите действующий адрес электронной почты.',                     
        widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    )
    password1 = forms.CharField(
        label='Password',
        widget=(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    )
    password2 = forms.CharField(
        label='Password Confirmation', 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}),
        help_text='Просто введите тот же пароль, для подтверждения'
    )