from django.http import HttpResponse, Http404
import datetime
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render

def current_datetime(request):
	now = datetime.datetime.now()
	return render(request, 'mytemplate.py',{'current_date': now})
