from django.db import models

# Create your models here.

# class Patient(models.Model):
#     patient_name = models.CharField(max_length=200)
#     patient_email = models.CharField(max_length=200)
#     patient_phone = models.CharField(max_length=200)
#     patient_message = models.TextField()
#     booked_date = models.DateField("date booked")

#     def __str__(self):
#         return self.patient_name


class student(models.Model):
    def __str__(self):
        return self.student_name
    student_name=models.CharField(max_length=200)
    student_contact=models.CharField(max_length=200)

class record(models.Model):
    patient_name = models.CharField(max_length=200)
    patient_email = models.CharField(max_length=200)
    patient_phone = models.CharField(max_length=200)
    patient_message = models.TextField()
    booked_date = models.DateField("date booked")

    def __str__(self):
        return self.patient_name



class reguser(models.Model):
    def __str__(self):
        return self.user_name
    user_name=models.CharField(max_length=200)
    user_email=models.CharField(max_length=200)
    user_phone=models.CharField(max_length=200)



class appointment(models.Model):
    patient_name = models.CharField(max_length=200)
    patient_email = models.CharField(max_length=200)
    patient_phone = models.CharField(max_length=200)
    patient_message = models.TextField()
    booked_date = models.DateField("date booked")

    def __str__(self):
        return self.patient_name

