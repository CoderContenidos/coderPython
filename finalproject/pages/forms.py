from django import forms
from .models import Page

class PageForm(forms.ModelForm):
    class Meta:

        model = Page
        fields = ['title', 'content', 'image', 'posted','order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Orden'}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'posted': forms.DateTimeInput(attrs={'class': 'datepicker'}),
        }
