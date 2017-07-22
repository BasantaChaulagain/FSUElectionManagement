from django.shortcuts import render, render_to_response
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from django.template.context_processors import csrf
from .models import Student

# Create your views here.

def index(request):
	t=loader.get_template('index.html')
	context = {}
	return HttpResponse(t.render(context))



def student(request):
	message = "Fill Up - Student Form"
	if request.method == "POST":
		t=loader.get_template('index.html')
		form = forms.StudentForm(request.POST, request.FILES)
		if form.is_valid():
			saved_form=form.save()
			context = { 'form_number':"Your form number"+saved_form.pk, 'message': "Form is received" }
			return HttpResponse(t.render(context))
	else:
		form = forms.StudentForm()
		token={}
		token.update(csrf(request))

	token = {'form':form, 'form_url':'student', 'message':message}
	return render(request, 'forms.html', token)


def candidate(request):
	message = "Fill Up - Candidate Form"
	if request.method == "POST":
		t=loader.get_template('index.html')
		form = forms.CandidateForm(request.POST, request.FILES)
		if form.is_valid():
			obj=form.save(commit=False)
			v_id=obj.voter_id
			if Student.objects.all().filter(voter_id = v_id).exists():
				student_object=Student.objects.get(voter_id = v_id)
				obj.election_id=1 #need to change later
				saved_form=obj.save()
				context = { 'form_number':"Your form number"+obj.candidate_id, 'message': "Form is received" }
				return HttpResponse(t.render(context))
			else:
				message = "You have not been registered as student. Get registered  before applying for the candidate."
		else:
			message="Registration Failed. Please try again."
	else:
		form= forms.CandidateForm()
		token={}
		token.update(csrf(request))

	token = {'form':form, 'message':message, 'form_url':'candidate'}
	return render(request, 'forms.html', token)


def viewdata(request):
	if request.method == "POST":
		t=loader.get_template('formDetails.html')
		querynum=request.POST.get("citz", "")
		if Student.objects.all().filter(citizenship_no = querynum).exists():
			result = Student.objects.all().filter(citizenship_no = querynum).values()
			img = result[0].get("photo")
		else:
			result = "Your data is not in the database."
		context = { 'result':result, 'img':img}
		return HttpResponse(t.render(context))

	else:
		t=loader.get_template('viewMyData.html')
		context={}
		context.update(csrf(request))
		return HttpResponse(t.render(context))
