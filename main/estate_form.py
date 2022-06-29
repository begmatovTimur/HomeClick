from django import forms
from .models import Estate, Category, CURRENCY, ESTATE_TYPE,    User


class EstateForm(forms.ModelForm):
    class Meta:
        model = Estate
        fields = '__all__'

    categories = forms.ModelMultipleChoiceField(
        queryset= Category.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )  
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}) 
    )
    description = forms.CharField(
        max_length=1000,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}) 
    )
    author = forms.ModelChoiceField(
        queryset= User.objects.all(),
        widget= forms.RadioSelect
    )
    price = forms.CharField(
        widget= forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите цену'})
    )   
    currency = forms.CharField(label='Currency', widget=forms.RadioSelect(choices=CURRENCY))
        
    area = forms.CharField(
        widget= forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите площадь' })
    )
    room_amount = forms.CharField(
        widget= forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите количество комнат' })
    )
    type = forms.CharField(
        label='Type', widget=forms.RadioSelect(choices=ESTATE_TYPE)
    )
    