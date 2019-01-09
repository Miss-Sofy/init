from django.db import models
from datetime import datetime
from django.conf import settings
 

# Create your models here.
Gender = (
     ('M', 'Male'),
     ('F', 'Female'),
     )

Student = (
     ('U', 'Undergraduate'),
     ('M', 'Masters'),
     ('PHD', 'PHD'),
     ('StudyAbroad','StudyAbroad'),

     )

Trainings = (
     ('Career', 'Career Development'),
     ('Application', 'Procedure & Application'),
     ('Interview Skills', 'Interview Skills'),
     ('StudyAbroad','StudyAbroad'),

     )

Duration = (
     ('T', 'Time'),
     ('D', 'Day'),
     ('W', 'Weeks'),
     ('M', 'Months'),
     ('Y', 'Years'),
     

     )
WriteUps = (
     ('Project', 'Project'),
     ('C.V', 'Curricullum Vitae'),

     )

Events_View = (
     ('Web', 'webinars'),
     ('Con', 'Conference'),
     ('Seminar', 'Seminars'),
     
     )
Opportunities = (
     ('Jobs', 'Jobs'),
     ('Grants', 'Grants'),

     )

Options = (
     ('Courses', 'Online Courses'),
     ('Materials', 'Materials'),
     ('Mentorship', 'Mentorship'),
     ('Trainings','Trainings'),

     )

    
class Hobby(models.Model):
     name = models.CharField(max_length=1000)

class Sport(models.Model):
     name = models.CharField(max_length=1000)

class Social_Media_accounts_name(models.Model):
     name = models.CharField(max_length=1000)
     username = models.CharField(max_length=1000)


class User(models.Model):
     Username = models.CharField(max_length=100)
     Email = models.EmailField ()
     password = models.CharField (max_length=10)
     Gender = models.CharField(max_length=2, choices=Gender)
     profile = models.CharField (max_length=1000)
     Hobbies = models.ManyToManyField(Hobby)
     Sports = models.ManyToManyField (Sport)
     Social_Media_accounts_names = models.ManyToManyField(Social_Media_accounts_name)

   
class Course(models.Model):
     course_name = models.CharField(max_length=64)
     course_code  = models.CharField(primary_key=True, max_length=20)
     course_module = models.CharField(max_length=1000)
     course_duration = models.CharField(max_length=4, choices=Duration,default='T')

class Mentor(models.Model):
     mentor_name = models.CharField(max_length=64)
     address = models.CharField (max_length=30)
     phone_number = models.CharField(max_length=25)
     email = models.EmailField ()
     gender = models.CharField(max_length=2, choices=Gender)
     hobbies = models.ManyToManyField(Hobby)
     media_account = models.ManyToManyField(Social_Media_accounts_name)

class Success_storie(models.Model):
     body = models.TextField()
     title = models.CharField(max_length=20)
     user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Event(models.Model):
     event_name = models.CharField(max_length=64)
     host = models.CharField(max_length=64)
     date_of_event = models.DateTimeField()
     Events_View = models.CharField(max_length=2, choices=Events_View, default='Seminars')

class Scholarship(models.Model):
     link = models.CharField(max_length=64)
     category  = models.CharField(max_length=20, choices=Student, default='Undergraduate')
     upload_at = models.DateTimeField(auto_now_add='True')

class Trainings_classe(models.Model):
     title = models.CharField(max_length=64)
     date_of_training = models.DateTimeField()
     type_of_training = models.CharField(max_length=20, choices=Trainings, default='career')
     additional = models.CharField(max_length=20, choices=WriteUps, default='C.V')

class Extra(models.Model):
     opportunity = models.CharField(max_length=20, choices=Opportunities, default='Jobs')
     additionals = models.CharField(max_length=20, choices=WriteUps, default='C.V')

class Document(models.Model):
     description = models.CharField(max_length=255, blank='True')
     document = models.FileField(upload_to='document')
     upload_at = models.DateTimeField(auto_now_add='True')

class Question(models.Model):
     questions = models.CharField(max_length=64)
     multiple_choices =  models.CharField (max_length=100)
