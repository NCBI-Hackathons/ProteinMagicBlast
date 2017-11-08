from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

# Create your views here.

def index(request):
	return HttpResponseRedirect('/smblast/')
