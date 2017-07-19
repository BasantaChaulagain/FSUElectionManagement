from django import forms
from . import models

class StudentForm(forms.ModelForm):
	class Meta:
		model=models.Student
		fields=['voter_id','name','sex','dob','disability','college_id','college','citizenship_no','photo']
