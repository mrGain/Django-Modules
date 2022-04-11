from django import forms

class ContactFrom(forms.Form):
    name =  forms.CharField(max_length=70, required=False)