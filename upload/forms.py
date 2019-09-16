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
    #style = "form-control col-form-label row"
    style = ""
    Reference_No = forms.CharField(widget=forms.TextInput(attrs={'class':style,}))
    Date_Time = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    Potassium = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    Sodium = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    Chloride = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    Urea= forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    Creatinine = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    T_Protein= forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    Albumin =  forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    Bilirubin  = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    AST  = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    ALP  = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    GGT = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    eGFR = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    Bicarbonate = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    File_name = forms.CharField(widget=forms.TextInput(attrs={'class': style, }), required=False)

    class Meta:
        model = BloodSamples
        fields = ('File_name','Reference_No','Date_Time','Potassium','Sodium','Chloride', 'Urea', 'Creatinine','T_Protein','Albumin','Bilirubin','AST','ALP','GGT','eGFR','Bicarbonate')

class BloodSampleForm2(forms.ModelForm):
    #style = "form-control col-form-label row"
    style = ""
    Reference_No = forms.CharField(widget=forms.TextInput(attrs={'class':style,}))
    Date_Time = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    HAEMOGLOBIN = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    RBC = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    PCV = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    MCV= forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    MCH = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    MCHC= forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    RDW =  forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    WCC  = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    Neutrophils  = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    Lymphocytes  = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    Monocytes = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    Eosinophils = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    Basophils = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    PLATELETS = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    ESR = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),required=False)
    File_name = forms.CharField(widget=forms.TextInput(attrs={'class': style, }), required=False)

    class Meta:
        model = BloodSamples2
        fields = ('File_name','Reference_No','HAEMOGLOBIN','Date_Time','RBC','PCV','MCV', 'MCH', 'MCHC','RDW','WCC','Neutrophils','Lymphocytes','Monocytes','Eosinophils','Basophils','PLATELETS','ESR')

class BloodSampleForm3(forms.ModelForm):
    style = ""
    Reference_No = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    Date_Time = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    Parathyroid_Hormone = forms.CharField(widget=forms.TextInput(attrs={'class': style, }), required=False)
    File_name = forms.CharField(widget=forms.TextInput(attrs={'class': style, }), required=False)

    class Meta:
        model = BloodSamples3
        fields = ('File_name','Reference_No','Date_Time','Parathyroid_Hormone')

class BloodSampleForm4(forms.ModelForm):
    style = ""
    Reference_No = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    Date_Time = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    Vitamin_D = forms.CharField(widget=forms.TextInput(attrs={'class': style, }), required=False)
    File_name = forms.CharField(widget=forms.TextInput(attrs={'class': style, }), required=False)

    class Meta:
        model = BloodSamples4
        fields = ('File_name','Reference_No','Date_Time','Vitamin_D')

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