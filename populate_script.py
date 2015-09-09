from portfolio.models import Project


oecd_project = Project(title='OECD Unemployment Visualization',
	description='A dynamic visualization of the unemployment rates in OECD countries over the past 15 years.',
	link='/portfolio/oecd_unemployment/',
	thumbnail='/static/images/oecd_unemployment_pic.png',
	tag_name = 'oecd')
oecd_tags = ['Python', 'Pandas library', 'Bokeh library']
oecd_project.save()

windchill_project = Project(title='Windchill Visualization',
	description='A dynamic, visual representation of the Siple windchill formula.',
	link='/portfolio/windchill/',
	thumbnail='/static/images/windchill_pic.png',
	tag_name='windchill')
windchill_tags = ['Python', 'Pandas library', 'Numpy library', 'Bokeh library']
windchill_project.save()

electronegativity_project = Project(title='Electronegativity Table',
	description='A dynamic representation of Periodic Table electronegativities.',
	link='/portfolio/electronegativity/',
	thumbnail='/static/images/electronegativity_pic.png',
	tag_name='electronegativity')
electronegativity_tags = ['Python', 'Bokeh library']
electronegativity_project.save()

geo_twitter_project = Project(title='Geo-Based Offline Sales Research',
	description='Project undertaken at Twitter to determine the offline '
	'sales impact of social networking platforms using a Geo-Based Methodology. '
	'Presented at QCon and Grace Hopper.',
	link='portfolio/geo_twitter/',
	tag_name='geo_twitter')
geo_twitter_project_tags = ['Python', 'R', 'Pandas library', 'Bash', 'Pig']
geo_twitter_project.save()

linear_regression_project = Project(title='Linear Regression Example',
	description = 'A simple, dynamic data visualization using Python\'s Pandas and Bokeh libraries.',
	link='portfolio/linear_regression/',
	tag_name='linear_regression')
linear_regression_tags = ['Python', 'Bokeh library']
linear_regression_project.save()

research_funding_project = Project(title='Research Funding Predictions Project',
	description='I explore the following research question: "What determines the levels of'
	'funding that an NSF or NASA-funded project receives?". I created a binary dependent '
	'variable that indicated whether the research project had received high levels of '
	'research funding. I defined high levels of research funding as the upper decile for '
	'the original, raw funding variable.\n'
	'I then utilized text analytics to determine the words in the abstract that were correlated\
	with high levels of funding. I utilized logit, CART, and Random Forest models. The initial '
	'iterations of all three models showed similar levels of accuracy, with an improvement of '
	'around 17% over the baseline. Ultimately, I chose to proceed with cross-validation with '
	'the logit and CART models -- while the Random Forest model performed a few fractions of a '
	'percentage point better than the CART model, it took substantially longer to train.\n'

	'After proceeding with cross-validation process, I found the logit model predicted whether '
	'a research project was likely to have received high levels of funding with around 89% accuracy '
	'on the testing sets, while the CART model predicted whether a research project was likely to '
	'have received high levels of funding with around 90% accuracy.\n'

	'Overall, I find the models provide a significant improvement over the baseline in predicting '
	'whether a research project is likely to be funded based solely on textual analysis of the '
	'abstract. I then repeated the analysis for other years in order to compare trends over time.',
	link='portfolio/research_funding/',
	tag_name='research_funding')
research_funding_tags = ['R', 'Machine Learning', 'ggplot2 Library']
research_funding_project.save()

#https://github.com/rowanv/pred-res-fund
#http://www.totiusmundi.com/QuantPortfolio/QuantPortfolio.html')

inclusion_with_identity_project = Project(title='Inclusion with Identity Dashboard',
	description = 'Created an online, interactive Tableau dashboard for the Inter-American'
	'Development Bank that visualized development indicators across various races'
	'and ethnicities in Latin America. Scraped national census data to create'
	'database that populated the dashboard.',
	link='portfolio/inclusion_with_identity/',
	tag_name='inclusion_with_identity')
inclusion_with_identity_tags = ['R', 'Tableau']

energy_industry_prediction_project = Project(title='Energy Industry Development Prediction',
	description = 'Used R to predict the development of the energy industry using'
	'a patent dataset. Determined whether certain technologies had reached a '
	'saturation point.',
	link='porfolio/energy_industry_prediction/',
	tag_name='energy_industry_prediction')
energy_industry_prediction_tags = ['R', 'ggplot2 Library']
energy_industry_prediction_project.save()

social_media_dashboard_project = Project(title='Social Media Dashboard',
	description = 'Created a real-time, dynamically updating social media dashboard that '
	'tracks a Twitter account\'s key use statistics.',
	link='porfolio/social_media_dashboard/',
	tag_name='social_media_dashboard')
social_media_dashboard_tags = ['Python', 'Bokeh library', 'Pandas library']
social_media_dashboard_project.save()

ith_degree_search_project = Project(title='Big Data Ith Degree Connections Finder',
	description = 'A Pig and Bash tool to find ith-degree connections for a list of '
	'1st-degree connections between nodes. This tool uses a Pig abstraction layer '
	'to create Map Reduce jobs that allow for scaling to a very large number '
	'of connections.',
	link='porfolio/ith_degree_search/',
	tag_name='ith_degree_search',)
ith_degree_search_tags = ['Pig', 'Bash', 'Map Reduce']
ith_degree_search_project.save()


