from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label='city', max_length=100)
    
