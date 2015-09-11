from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import os

from portfolio.models import Project, Skill



def portfolio(request):
	return render(request, 'portfolio.html', {'projects_list': Project.objects.all(),
		'all_skills_list': [o.name for o in Skill.objects.all()]})

def about(request):
	return render(request, 'about.html')

def skills(request):
	return render(request, 'skills.html')

def contact(request):
	return render(request, 'contact.html')


## Visualization Views ######

def windchill(request):
	return render(request, 'visualizations/windchill_table.html')

def oecd_unemployment(request):
	return render(request, 'visualizations/oecd_unemployment.html')

def electronegativity(request):
	with open('portfolio/templates/visualizations/electronegativity_table.html') as myfile:
		data = "\n".join(line for line in myfile)
	return HttpResponse(data)

## Project Views #######
def geo_twitter(request):
	return render(request, 'project_pages/geo_twitter.html')

def research_funding(request):
	return render(request, 'project_pages/research_funding.html')




