from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import os

from portfolio.models import Project



def portfolio(request):
	return render(request, 'portfolio.html', {'projects_list': Project.objects.all()})

def windchill(request):
	with open('portfolio/templates/visualizations/windchill_table.html') as myfile:
		data = "\n".join(line for line in myfile)
	return HttpResponse(data)

def oecd_unemployment(request):
	with open('portfolio/templates/visualizations/oecd_unemployment.html') as myfile:
		data = "\n".join(line for line in myfile)
	return HttpResponse(data)
