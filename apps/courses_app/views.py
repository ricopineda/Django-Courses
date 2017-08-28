from __future__ import unicode_literals
from models import *
from django.shortcuts import render, HttpResponse, redirect
import random
from django.contrib import messages

def index(request):

	context = {
	'course': Course.objects.all()
	}

	return render(request, 'courses_app/index.html', context)


def add(request):	
	name = request.POST['name']
	desc = request.POST['desc']

	print("Inside add", name, desc)

	Course.objects.create(name=name, desc=desc)



	return redirect('/')

def delete(request, id):
	context = {
	'course': Course.objects.get(id=id)
	}
	return render(request, 'courses_app/delete.html', context )

def confirm_delete(request, id):

	a = Course.objects.get(id=id)
	a.delete()
	# a.save()

	return redirect('/')