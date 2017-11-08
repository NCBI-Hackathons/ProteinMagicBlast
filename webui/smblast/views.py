from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template import loader
from django.views.static import serve
from smblast.core.process import *
import uuid

# Create your views here.

def index(request):
    template = loader.get_template('smblast/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def run(request):
	process = Process(request.POST['user_id'])
	process.Run(request.POST['srr'], request.POST['protein'])
	return HttpResponseRedirect('/smblast/progress/?user_id=' + request.POST['user_id'])

def progress(request):
	template = loader.get_template('smblast/progress.html')
	context = {
		'user_id' : str(request.GET['user_id'])
	}
	return HttpResponse(template.render(context, request))

def progressGet(request):
	process = Process(request.POST['user_id'])
	return JsonResponse(process.GetProgress())

def result(request):
	user_id = request.GET['user_id']
	context = {
		'user_id' : str(user_id)
	}

	process = Process(user_id)
	progress = process.GetProgress()
	if 'error' in progress and progress['error']:
	    template = loader.get_template('smblast/error.html')
	    context['log'] = process.GetLog()
	    return HttpResponse(template.render(context, request))

	template = loader.get_template('smblast/result.html')
	context['result'] = process.GetResult()
	return HttpResponse(template.render(context, request))

def resultDownload(request):
	user_id = request.GET['user_id']
	process = Process(user_id)
	filepath = process.GetResultFilePath()
	return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

