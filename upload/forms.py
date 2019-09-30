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
    # making all fields mandatory else it wont be able to pushed it up to DB
    style = ""
    Reference_No = forms.CharField(widget=forms.TextInput(attrs={'class':style,}))
    Date_Time = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    Potassium = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),)
    Sodium = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),)
    Chloride = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),)
    Urea= forms.CharField(widget=forms.TextInput(attrs={'class': style, }),)
    Creatinine = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),)
    T_Protein= forms.CharField(widget=forms.TextInput(attrs={'class': style, }),)
    Albumin =  forms.CharField(widget=forms.TextInput(attrs={'class': style, }),)
    Bilirubin  = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),)
    AST  = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),)
    ALP  = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),)
    GGT = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),)
    eGFR = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),)
    Bicarbonate = forms.CharField(widget=forms.TextInput(attrs={'class': style, }),)
    File_name = forms.CharField(widget=forms.TextInput(attrs={'class': style, }), )

    class Meta:
        model = BloodSamples
        fields = ('File_name','Reference_No','Date_Time','Potassium','Sodium','Chloride', 'Urea', 'Creatinine','T_Protein','Albumin','Bilirubin','AST','ALP','GGT','eGFR','Bicarbonate')

class BloodSampleForm2(forms.ModelForm):
    #style = "form-control col-form-label row"
    #making all fields mandatory else it wont be able to pushed it up to DB
    style = ""
    Reference_No = forms.CharField(widget=forms.TextInput(attrs={'class':style,}))
    Date_Time = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    HAEMOGLOBIN = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    RBC = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    PCV = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    MCV= forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    MCH = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    MCHC= forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    RDW =  forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    WCC  = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    Neutrophils  = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    Lymphocytes  = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    Monocytes = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    Eosinophils = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    Basophils = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    PLATELETS = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    ESR = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    File_name = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))

    class Meta:
        model = BloodSamples2
        fields = ('File_name','Reference_No','HAEMOGLOBIN','Date_Time','RBC','PCV','MCV', 'MCH', 'MCHC','RDW','WCC','Neutrophils','Lymphocytes','Monocytes','Eosinophils','Basophils','PLATELETS','ESR')

class BloodSampleForm3(forms.ModelForm):
    # making all fields mandatory else it wont be able to pushed it up to DB
    style = ""
    Reference_No = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    Date_Time = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    Parathyroid_Hormone = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    File_name = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))

    class Meta:
        model = BloodSamples3
        fields = ('File_name','Reference_No','Date_Time','Parathyroid_Hormone')

class BloodSampleForm4(forms.ModelForm):
    # making all fields mandatory else it wont be able to pushed it up to DB
    style = ""
    Reference_No = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    Date_Time = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    Vitamin_D = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))
    File_name = forms.CharField(widget=forms.TextInput(attrs={'class': style, }))

    class Meta:
        model = BloodSamples4
        fields = ('File_name','Reference_No','Date_Time','Vitamin_D')

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control form-control-user",}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control form-control-user",}))
    class Meta:
        model = Login

        fields = ('username','password')

class Search(forms.ModelForm):
    search = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))

    class Meta:
        model = Search

        fields = ('search',)

class RetrieveAllBlood(forms.ModelForm):

    Reference_No = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    Date_Time = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    Vitamin_D = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    Parathyroid_Hormone = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    HAEMOGLOBIN = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    RBC = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    PCV = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    MCV = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    MCH = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    MCHC = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    RDW = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    WCC = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    Neutrophils = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    Lymphocytes = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    Monocytes = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    Eosinophils = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    Basophils = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    PLATELETS = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    ESR = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    Sodium = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    Potassium = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    Chloride = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    Urea = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    Creatinine = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    T_Protein = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    Albumin = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    Bilirubin = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    AST = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    ALP = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    GGT = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    eGFR = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))
    Bicarbonate = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",}))

    class Meta:
        model = RetrieveAllBlood

        fields = ('Reference_No', 'Date_Time','HAEMOGLOBIN','RBC', 'PCV', 'MCV', 'MCH', 'MCHC', 'RDW', 'WCC',
        'Neutrophils', 'Lymphocytes', 'Monocytes', 'Eosinophils', 'Basophils', 'PLATELETS', 'ESR','Vitamin_D','Parathyroid_Hormone',
        'Potassium', 'Sodium', 'Chloride', 'Urea', 'Creatinine', 'T_Protein','Albumin', 'Bilirubin', 'AST', 'ALP', 'GGT', 'eGFR', 'Bicarbonate')


class null(forms.ModelForm):
    class Meta:
        model = BloodSamples2
        fields = ()