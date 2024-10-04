from django import forms

class userForms(forms.Form):
    num1 = forms.CharField(label="value1",required=False,widget=forms.TextInput(attrs={'class':'user-form'}))
    num2 = forms.CharField(label="value2")
    num3 = forms.CharField(label="value3")
    email=forms.EmailField()