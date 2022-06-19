from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def say_hello(request):
	# can pull data from db
	# transform
	# send email, etc
	return HttpResponse('Hello world')