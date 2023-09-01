from django.db import models

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES= [
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    ]
 
    MAJOR_CHOICES = [
        ('Computer Science', 'Computer Science'),
        ('Engineering', 'Engineering'),
        ('Business', 'Business')
   ]

    studentName= models.CharField(max_length=50)
    studentId= models.CharField(max_length=30,unique=True)
    gender= models.CharField(max_length=20,choices=GENDER_CHOICES)
    date_of_Birth=models.DateField()
    major= models.CharField(max_length=50,choices=MAJOR_CHOICES)
    email= models.EmailField(unique=True)
    contact_number=models.CharField(max_length=20)
    class Meta:
         db_table="Student"





