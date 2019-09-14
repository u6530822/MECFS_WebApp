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
    style = "form-control col-form-label row"
    '''Reference_No = forms.CharField(widget=forms.TextInput(attrs={'class':style,}))
    Date_Time = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    Potassium = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    Sodium = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    Chloride = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    Urea= forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    Creatinine = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    T_Protein= forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    Albumin =  forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    Bilirubin  = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    AST  = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    ALP  = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    GGT = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    eGFR = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    Bicarbonate = forms.CharField(widget=forms.TextInput(attrs={'class': style, })) '''

    class Meta:
        model = BloodSamples
        fields = ('Reference_No','Date_Time','Potassium','Sodium','Chloride', 'Urea', 'Creatinine','T_Protein','Albumin','Bilirubin','AST','ALP','GGT','eGFR','Bicarbonate')

class BloodSampleForm2(forms.ModelForm):
    class Meta:
        model = BloodSamples2
        fields = ('Reference_No','HAEMOGLOBIN','Date_Time','RBC','PCV','MCV', 'MCH', 'MCHC','RDW','WCC','Neutrophils','Lymphocytes','Monocytes','Eosinophils','Basophils','PLATELETS','ESR')

class BloodSampleForm3(forms.ModelForm):
    class Meta:
        model = BloodSamples3
        fields = ('Reference_No','Date_Time','Parathyroid_Hormone')

class BloodSampleForm4(forms.ModelForm):
    class Meta:
        model = BloodSamples4
        fields = ('Reference_No','Date_Time','Vitamin_D')

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control form-control-user",}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control form-control-user",}))
    class Meta:
        model = Login

        fields = ('username','password')

class null(forms.ModelForm):
    class Meta:
        model = BloodSamples2
        fields = ()