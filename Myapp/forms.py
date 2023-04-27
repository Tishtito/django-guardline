from django import forms
from Myapp.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields=['firstname','lastname','age','phonenumber']

class Employeeform(forms.Form):
    firstname=forms.CharField(label="Enter firstname",max_length=50)
    lastname=forms.CharField(label="Enter lastname",max_length=50)
    age=forms.IntegerField(label="Enter age")
    phonenumber=forms.IntegerField(label="Phonenumber",)




