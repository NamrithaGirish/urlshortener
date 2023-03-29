from django import forms

class UrlForm(forms.Form):
    org=forms.URLField(label="url",required=True)