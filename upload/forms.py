from django import forms
from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text','extra','insert')


class ResultsPage(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text','title')

class BloodSampleForm(forms.ModelForm):
    class Meta:
        model = BloodSamples
        fields = ('Reference','LabNo','Date_Time','Potassium','Sodium','Chloride','MCH')






