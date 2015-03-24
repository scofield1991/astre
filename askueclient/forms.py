from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your fucking name', max_length=100, min_length=1)
