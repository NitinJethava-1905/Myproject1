from django.db import models

# Create your models here.

class SignupMaster(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    zipcode=models.IntegerField()

class careermaster(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    experience=models.CharField(max_length=20)
    applyfor=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    aboutself=models.TextField()
    resume=models.FileField(upload_to='MyFiles')

class inquirymaster(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    inquiry1=models.CharField(max_length=30)
    inquiry2=models.CharField(max_length=30)
    address=models.TextField()
    message=models.TextField()
