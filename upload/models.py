# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    extra = models.CharField(max_length=200)
    insert = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class BloodSamples(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Reference_No = models.CharField(max_length=100)
    Sodium = models.CharField(max_length=200)
    Potassium = models.CharField(max_length=200)
    Chloride = models.CharField(max_length=200)
    Date_Time = models.CharField(max_length=200)
    Urea= models.CharField(max_length=200)
    Creatinine = models.CharField(max_length=200)
    T_Protein= models.CharField(max_length=200)
    Albumin = models.CharField(max_length=200)
    Bilirubin = models.CharField(max_length=200)
    AST = models.CharField(max_length=200)
    ALP = models.CharField(max_length=200)
    GGT= models.CharField(max_length=200)
    eGFR = models.CharField(max_length=200)
    Bicarbonate = models.CharField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Reference

class BloodSamples2(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Reference_No = models.CharField(max_length=200)
    Date_Time= models.CharField(max_length=200)
    HAEMOGLOBIN = models.CharField(max_length=200)
    RBC = models.CharField(max_length=200)
    PCV = models.CharField(max_length=200)
    MCV = models.CharField(max_length=200)
    MCH = models.CharField(max_length=200)
    MCHC= models.CharField(max_length=200)
    RDW = models.CharField(max_length=200)
    WCC= models.CharField(max_length=200)
    Neutrophils = models.CharField(max_length=200)
    Lymphocytes = models.CharField(max_length=200)
    Monocytes = models.CharField(max_length=200)
    Eosinophils = models.CharField(max_length=200)
    Basophils= models.CharField(max_length=200)
    PLATELETS = models.CharField(max_length=200)
    ESR = models.CharField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Reference

class BloodSamples3(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Reference_No = models.CharField(max_length=200)
    Date_Time= models.CharField(max_length=200)
    Parathyroid_Hormone= models.CharField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Reference

class BloodSamples4(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Reference_No = models.CharField(max_length=200)
    Date_Time= models.CharField(max_length=200)
    Vitamin_D= models.CharField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Reference


class Login(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.username