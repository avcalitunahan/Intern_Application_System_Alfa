from koustaj.models import OgrenciBasvuru
from django import forms
class basvuruForm(forms.ModelForm):
    
    class Meta:
        model = OgrenciBasvuru
        fields = '__all__'
