from django import forms
from .models import Database, Search

class Database_form(forms.ModelForm):
    
    class Meta: 
        model = Database
        fields = ('criminal_name', 'criminal_img', 'encodings')
        widgets = {'encodings': forms.HiddenInput()}
    
    def __init__(self, *args, **kwargs):
        super(Database_form, self).__init__(*args, **kwargs)
        self.fields['encodings'].required = False

class Search_form(forms.ModelForm):
    
    class Meta: 

        model = Search
        fields = ('criminal_name', 'criminal_img')

