from django.shortcuts import render
from django.http import HttpResponse

from models import Poll, Choice
# Create your views(functions) here.
# Remember each function/view the first argument/input has to be request

def princesses(request):
	return "Let it go! LET IT GOO!"