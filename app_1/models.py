from django.db import models
# Create your models here.

class Student(models.Model):
    blood_group_ch = [
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('O+','O+'),
        ('O-','O-'),
    ]
    name = models.CharField(max_length=50)
    std = models.SmallIntegerField()
    roll_no = models.CharField(max_length=10)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    address = models.TextField(max_length=200)
    blood_group = models.CharField(max_length=3, choices=blood_group_ch)

    def __str__(self):
        return f"{self.name}"