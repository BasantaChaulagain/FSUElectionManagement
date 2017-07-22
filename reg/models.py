
from __future__ import unicode_literals
from django import forms
from django.db import models


gender = (
    ('Male', 'Male'), #(what to be entered, what to be shown)
    ('Female', 'Female'),
)



class Student(models.Model):
    voter_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=6,choices=gender,default='Male')
    dob = models.DateField()
    disability = models.CharField(max_length=50)
    college_id = models.CharField(max_length=9)
    college = models.IntegerField()
    citizenship_no = models.CharField(max_length=20)
    photo = models.FileField(upload_to='student-photo')
    is_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'student'

    def __str__(self):              
        return (str(self.voter_id)+'    |    '+self.name+'    |    '+self.citizenship_no)



class Candidate(models.Model):
    voter_id = models.IntegerField()
    candidate_id = models.AutoField(primary_key=True)
    party_id = models.IntegerField()
    election_id = models.IntegerField()
    post = models.CharField(max_length=50)
    college_id = models.CharField(max_length=9)
    college = models.IntegerField()
    votes = models.IntegerField(default=0)
    symbol = models.FileField(upload_to='candidate-symbol')
    is_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'candidate'

    def __str__(self):              
        return (str(self.candidate_id)+'    |    '+str(self.post)+'    |    '+str(self.party_id))


class College(models.Model):
    college_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'college'



class Election(models.Model):
    election_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    year = models.TextField()  # This field type is a guess.

    class Meta:
        db_table = 'election'


class Party(models.Model):
    party_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    registration_no = models.IntegerField()
    symbol = models.TextField()

    class Meta:
        db_table = 'party'


class Staff(models.Model):
    staff_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=6)
    citizenship_no = models.IntegerField()
    college = models.IntegerField()
    position = models.CharField(max_length=50)
    photo = models.IntegerField()
    dob = models.DateField()
    citizenship_scan = models.TextField()

    class Meta:
        db_table = 'staff'




class WinnerReport(models.Model):
    post = models.CharField(primary_key=True,max_length=50)
    candidate_id = models.IntegerField()
    votes = models.IntegerField()
    election_id = models.IntegerField()

    class Meta:
        db_table = 'winner_report'
