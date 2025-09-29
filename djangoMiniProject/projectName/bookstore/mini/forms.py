# mini/forms.py
from django import forms
from django.core.validators import URLValidator

class URLForm(forms.Form):
    url = forms.URLField(
        label='Enter a URL',
        validators=[URLValidator()],
        widget=forms.TextInput(attrs={'placeholder': 'https://example.com/'})
    )