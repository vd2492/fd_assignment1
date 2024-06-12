# permapp/forms.py
from django import forms

class WordForm(forms.Form):
    word = forms.CharField(max_length=5, min_length=3, required=True, label="Enter a word (3 to 5 letters)")
