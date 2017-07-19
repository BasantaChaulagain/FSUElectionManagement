from django.shortcuts import render, render_to_response
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from django.template.context_processors import csrf
from .models import Student

# Create your views here.

def index(request):
	t=loader.get_template('index.html')
	context = {'message':'Hey, this is working !'}
	return HttpResponse(t.render(context))



def student(request):
	if request.method == "POST":
		t=loader.get_template('index.html')
		form = forms.StudentForm(request.POST, request.FILES)
		if form.is_valid():
			saved_form=form.save()
			context = { 'form_number':saved_form.pk, 'message': "numbered form is received" }
			return HttpResponse(t.render(context))
	else:
		form = forms.StudentForm()
		token={}
		token.update(csrf(request))

	token = {'form':form}
	return render(request, 'forms.html', {'form': form})


def viewdata(request):
	if request.method == "POST":
		t=loader.get_template('formDetails.html')
		querynum=request.POST.get("citz", "")
		if Student.objects.all().filter(citizenship_no = querynum).exists():
			result = Student.objects.all().filter(citizenship_no = querynum).values()
		else:
			result = "Your data is not in the database."

		context = { 'result':result }
		return HttpResponse(t.render(context))

	else:
		t=loader.get_template('viewMyData.html')
		context={}
		context.update(csrf(request))
		return HttpResponse(t.render(context))
