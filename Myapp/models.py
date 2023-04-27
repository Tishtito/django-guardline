from django.db import models

# Create your models here.
class Student(models.Model):
    firstname= models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    age=models.IntegerField(null=True)
    phonenumber=models.IntegerField(null=True)

    class meta:
        db_table="Student"

    def __str__(self):
        return self.firstname+' '+self.lastname

class Employee(models.Model):
    name=models.CharField(max_length=20)
    postion=models.CharField(max_length=20)
    office=models.CharField(max_length=20)
    age=models.IntegerField(null=True)
    startdate=models.DateField(null=True)
    salary=models.IntegerField(null=True)

    class meta:
        db_table="Employee"

    def __str__(self):
        return self.name

class Add_Venue(models.Model):
    VenueName=models.CharField(max_length=20)
    Address=models.CharField(max_length=20)
    Zipcode=models.IntegerField(null=True)
    Phonenumber=models.IntegerField(null=True)
    Webadress=models.IntegerField(null=True)
    Emailaddress=models.CharField(max_length=20)


class Add_Post(models.Model):
    Author=models.CharField(max_length=10)
    Title=models.CharField(max_length=20)
    Text=models.TextField(null=True)
    Created_date=models.DateTimeField(null=True)
    Published_date=models.DateTimeField(null=True)



