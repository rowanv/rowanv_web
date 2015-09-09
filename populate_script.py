from portfolio.models import Project


oecd_project = Project(title='OECD Unemployment Visualization',
	description='A dynamic visualization of the unemployment rates in OECD countries over the past 15 years.',
	link='/portfolio/oecd_unemployment/',
	thumbnail='/static/images/oecd_unemployment_pic.png')
oecd_tags = ['Python', 'Pandas library', 'Bokeh library']
oecd_project.save()

windchill_project = Project(title='Windchill Visualization',
	description='A dynamic, visual representation of the Siple windchill formula.',
	link='/portfolio/windchill/',
	thumbnail='/static/images/windchill_pic.png')
windchill_tags = ['Python', 'Pandas library', 'Numpy library', 'Bokeh library']
windchill_project.save()