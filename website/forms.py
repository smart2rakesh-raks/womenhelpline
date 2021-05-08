
from  django import forms

class AddComplaintForm(forms.Form):


    cpname=forms.CharField(max_length=4000)
    ctitle=forms.CharField(max_length=4000)
    cdes=forms.CharField(max_length=20000)
    cimage1=forms.FileField()
    cimage2 = forms.FileField()
    cimage3 =forms.FileField()
    cagainstname=forms.CharField(max_length=4000)
    csubmiterphone=forms.CharField(max_length=4000)


