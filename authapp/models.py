from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField
    phonenumber=models.CharField(max_length=25)
    description=models.TextField

    def __str__(self):
        return self.email
    
class Enrollment(models.Model):
    Fullname=models.CharField(max_length=25)
    Email=models.EmailField()
    Gender=models.CharField(max_length=25)
    Phonenumber=models.CharField(max_length=12)
    DOB=models.CharField(max_length=25)
    SelectMembershipplan=models.CharField(max_length=205)
    Selecttrainer=models.CharField(max_length=205)
    Reference=models.CharField(max_length=55)
    Address=models.TextField()
    paymentstatus=models.CharField(max_length=55,blank=True,null=True)
    price=models.IntegerField(blank=True,null=True)
    Duedate=models.DateTimeField(blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.Fullname
    
class Trainer(models.Model):
    name=models.CharField(max_length=25)
    gender=models.CharField(max_length=25)
    phone=models.CharField(max_length=12)
    salary=models.IntegerField(max_length=25)
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.name

class Membershipplan(models.Model):
    plan=models.CharField(max_length=25)
    price=models.IntegerField(max_length=25)

    def __str__(self):
        return self.id

