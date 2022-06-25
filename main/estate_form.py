from django import forms
from .models import Estate, Category, CURRENCY, ESTATE_TYPE


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
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}) 
    )
    description = forms.CharField(
        max_length=1000,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'text'}) 
    )
    price = forms.CharField(
        widget= forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'price'})
    )   
    currency = forms.CharField(label='Currency', widget=forms.RadioSelect(choices=CURRENCY))
        
    area = forms.CharField(
        widget= forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'area' })
    )
    room_amount = forms.CharField(
        widget= forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'room amout' })
    )
    type = forms.CharField(
        label='Type', widget=forms.RadioSelect(choices=ESTATE_TYPE)
    )
    