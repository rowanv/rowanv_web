from portfolio.models import Project


p = Project(title='OECD Unemployment Visualization',
	description='A dynamic visualization of the unemployment rates in OECD countries over the past 15 years.',
	link='/portfolio/oecd_unemployment/')
p.save()