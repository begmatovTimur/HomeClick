from django import forms


class LoginForm(forms.Form):
    class Meta(forms.Form):
        fields = ('username', 'password')


    username = forms.CharField(
        max_length=30,
        min_length=5,
        required=True,
        widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    )

    password = forms.CharField(
        label='Password',
        widget=(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Type password'}))
    )