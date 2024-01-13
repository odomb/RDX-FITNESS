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
    salary=models.IntegerField()
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.name

class Membershipplan(models.Model):
    plan=models.CharField(max_length=25)
    price=models.IntegerField()

    def __str__(self):
        return self.id


class Gallery(models.Model):
    title=models.CharField(max_length=100)
    img=models.ImageField(upload_to='gallery')
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __int__(self):
        return self.id


class Attendance(models.Model):
    Selectdate=models.DateTimeField(auto_now_add=True)
    phonenumber=models.CharField(max_length=15)
    Login=models.CharField(max_length=200)
    Logout=models.CharField(max_length=200)
    SelectWorkout=models.CharField(max_length=200)
    TrainedBy=models.CharField(max_length=200)
    def __int__(self):
        return self.id

