from django import forms
class inputform(forms.Form):
    input1=forms.IntegerField(min_value=0,max_value=20,label="Enter a number")