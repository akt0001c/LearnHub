from django.db import models

# Create your models here.

class Instructor(models.Model):
    GENDER_CHOICES= [
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    ]
 
    MAJOR_CHOICES = [
        ('Science', 'Science'),
        ('Engineering', 'Engineering'),
        ('Arts', 'Arts')
   ]
    

    instructorName = models.CharField(max_length=20)
    gender= models.CharField(max_length=15,choices=GENDER_CHOICES)
    date_of_birth= models.DateField()
    department= models.CharField(max_length=30,choices=MAJOR_CHOICES)
    email=models.EmailField()
    contact_no=models.CharField(max_length=15)
    class Meta:
         db_table="Instructor"
