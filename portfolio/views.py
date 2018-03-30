from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

from portfolio.models import Project, Skill, PastWorkEngagement


def portfolio(request):
    return render(request, 'portfolio_home.html', {
        'projects_list': Project.objects.all(),
        'top_past_work_engagement_list': PastWorkEngagement.objects.all()[:3]})


def about(request):
    '''
    Display about page.

    **Template**:
    :template:`about.html`
    '''
    return render(request, 'about.html')


class PortfolioProjectsView(ListView):

    model = Project
    template_name = 'portfolio_projects.html'


class ServicesView(ListView):

    model = PastWorkEngagement
    template_name = 'services.html'


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
