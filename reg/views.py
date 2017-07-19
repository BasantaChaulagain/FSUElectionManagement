from django.shortcuts import render, render_to_response
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from django.template.context_processors import csrf

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
			#saved_form=form(commit=False)
			#saved_form.is_verified=False
			#saved_form.photo = request.FILES.get('photo')
			saved_form=form.save()
			context = { 'form_number':saved_form.pk, 'message': "numbered form is received" }
			return HttpResponse(t.render(context))

	else:
		form = forms.StudentForm()
		token={}
		token.update(csrf(request))

	token = {'form':form}
	return render(request, 'forms.html', {'form': form})

