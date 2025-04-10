import sys

try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()


# Sample User model
class User(models.Model):
    name = models.CharField(max_length=50, default="Dan")

    def __str__(self):
        return self.name


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["headline"]

    def __str__(self):
	    return self.headline

class Student(models.Model):
    #student_id = models.IntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    graduation_year = models.IntegerField()
    student_email = models.EmailField()


class Attendance(models.Model):
    #attendance_id = models.IntegerField()
    date = models.DateTimeField() 
    attendance_status = models.BooleanField()
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE) 

class Event(models.Model):
    event_name = models.CharField(max_length=30)
    event_start = models.DateTimeField() 
    event_end = models.DateTimeField() 
    event_coordinator = models.CharField(max_length=30)
    approval = models.BooleanField()

class Admin(models.Model):
    admin_email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    job_title = models.CharField(max_length=30)
    room_number = models.IntegerField()

class Event_approver(models.Model):
    event_name = models.CharField(max_length=30)
    admin_email = models.EmailField()
    individual_approval_status = models.BooleanField()
    # pk = models.CompositePrimaryKey("event_name", "admin_email")
    event_name = models.ForeignKey(Event, on_delete=models.CASCADE) 
    admin_email = models.ForeignKey(Admin, on_delete=models.CASCADE) 

