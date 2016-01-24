from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic import TemplateView
import os

from portfolio.models import Project, Skill


def portfolio(request):
    return render(request, 'portfolio.html', {'projects_list': Project.objects.all(),
                                              'all_skills_list': [o.name for o in Skill.objects.all()]})


def about(request):
    return render(request, 'about.html')


def skills(request):
    return render(request, 'skills.html')


def resume(request):
    return render(request, 'resume.html')


def contact(request):
    return render(request, 'contact.html')


class BookView(TemplateView):
    template_name = 'book.html'


## Visualization Views ######

def windchill(request):
    return render(request, 'visualizations/windchill_table.html')


def oecd_unemployment(request):
    return render(request, 'visualizations/oecd_unemployment.html')


def electronegativity(request):
    return render(request, 'visualizations/electronegativity_table.html')


def housing_prices(request):
    return render(request, 'visualizations/housing_prices.html')


def gender_olympics_viz(request):
    return render(request, 'visualizations/gender_olympics_viz.html')


def brazil_map(request):
    return render(request, 'visualizations/brazil_map.html')


def voter_turnout_viz(request):
    return render(request, 'visualizations/voter_turnout_presidential_line_graph.html')

## Project Views #######


def geo_twitter(request):
    return render(request, 'project_pages/geo_twitter.html')


def research_funding(request):
    return render(request, 'project_pages/research_funding.html')


def gender_olympics(request):
    return render(request, 'project_pages/gender_olympics.html')


def gender_olympics_ipython(request):
    return render(request, 'project_pages/Olympic Medal Count Bar Chart - Data Cleaning.html')


def voter_turnout(request):
    return render(request, 'project_pages/voter_turnout.html')


def voter_turnout_ipython(request):
    return render(request,
                  'project_pages/Voter Turnout Data Cleaning and Analysis.html')


def business_dash(request):
    return render(request,
                  'project_pages/business_dash.html')
