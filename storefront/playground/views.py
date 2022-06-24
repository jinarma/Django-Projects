from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def say_hello(request):
	# can pull data from db
	# transform
	# send email, etc
	return HttpResponse('Hello world')

def show_sum(request):
	sum_till_now = 0
	for i in range(1, 101):
		sum_till_now += i
		print(f'{i} - {sum_till_now}')