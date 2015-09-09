from portfolio.models import Skill, Project


r_skill = Skill(name='R')
r_skill.save()

python_skill = Skill(name='Python')
python_skill.save()

pandas_library_skill = Skill(name='Pandas Library')
pandas_library_skill.save()

bokeh_library_skill = Skill(name='Bokeh Library')
bokeh_library_skill.save()

numpy_library_skill = Skill(name='Numpy Library')
numpy_library_skill.save()

bash_skill = Skill(name='Bash')
bash_skill.save()

pig_skill = Skill(name='Pig')
pig_skill.save()

machine_learning_skill = Skill(name='Machine Learning')
machine_learning_skill.save()

ggplot2_library_skill = Skill(name='ggplot2 Library')
ggplot2_library_skill.save()

tableau_skill = Skill(name='Tableau')
tableau_skill.save()

map_reduce_skill = Skill(name='Map Reduce')
map_reduce_skill.save()

hadoop_skill = Skill(name='Hadoop')
hadoop_skill.save()



oecd_project = Project(title='OECD Unemployment Visualization',
	description='A dynamic visualization of the unemployment rates in OECD countries over the past 15 years.',
	link='/portfolio/oecd_unemployment/',
	thumbnail='/static/images/oecd_unemployment_pic.png',
	tag_name = 'oecd')
oecd_project.save()
oecd_project.skills_list.add(r_skill, pandas_library_skill, bokeh_library_skill)
oecd_project.save()

windchill_project = Project(title='Windchill Visualization',
	description='A dynamic, visual representation of the Siple windchill formula.',
	link='/portfolio/windchill/',
	thumbnail='/static/images/windchill_pic.png',
	tag_name='windchill')
windchill_project.save()
windchill_project.skills_list.add(python_skill, pandas_library_skill, bokeh_library_skill, numpy_library_skill)
windchill_project.save()

ith_degree_search_project = Project(title='Big Data Ith Degree Connections Finder',
	description = 'A Pig and Bash tool to find ith-degree connections for a list of '
	'1st-degree connections between nodes. This tool uses a Pig abstraction layer '
	'to create Map Reduce jobs that allow for scaling to a very large number '
	'of connections.',
	thumbnail='/static/images/ith_degree_search_pic.png',
	link='porfolio/ith_degree_search/',
	tag_name='ith_degree_search',)
ith_degree_search_project.save()
ith_degree_search_project.skills_list.add(pig_skill, bash_skill, map_reduce_skill, hadoop_skill)
ith_degree_search_project.save()

electronegativity_project = Project(title='Electronegativity Table',
	description='A dynamic representation of Periodic Table electronegativities.',
	link='/portfolio/electronegativity/',
	thumbnail='/static/images/electronegativity_pic.png',
	tag_name='electronegativity')
electronegativity_project.save()
electronegativity_project.skills_list.add(python_skill, bokeh_library_skill)
electronegativity_project.save()

geo_twitter_project = Project(title='Geo-Based Offline Sales Research',
	description='Project undertaken at Twitter to determine the offline '
	'sales impact of social networking platforms using a Geo-Based Methodology. '
	'Presented at QCon and Grace Hopper.',
	link='portfolio/geo_twitter/',
	thumbnail='/static/images/abstract_green.png',
	tag_name='geo_twitter')
geo_twitter_project.save()
geo_twitter_project.skills_list.add(python_skill, r_skill, pandas_library_skill, bash_skill, pig_skill, hadoop_skill)
geo_twitter_project.save()

linear_regression_project = Project(title='Linear Regression Example',
	description = 'A simple, dynamic data visualization using Python\'s Pandas and Bokeh libraries.',
	link='portfolio/linear_regression/',
	thumbnail='/static/images/linear_regression_pic.png',
	tag_name='linear_regression')
linear_regression_project.save()
linear_regression_project.skills_list.add(python_skill, bokeh_library_skill)
linear_regression_project.save()

research_funding_project = Project(title='Research Funding Predictions Project',
	description='I explore the following research question: "What determines the levels of'
	'funding that an NSF or NASA-funded project receives?".  I define high levels of research' 
	'funding as the upper decile for the original, raw funding variable. I then use text '
	'analytics to determine the words in the abstract that were correlated'
	'with high levels of funding. Using CART, logistic regression, and Random Forest models,'
	'I am able to predict whether a research project is likely to have received high levels of funding'
	'with around 90% accuracy.',
	link='portfolio/research_funding/',
	thumbnail='/static/images/research_funding_pic.png',
	tag_name='research_funding')
research_funding_project.save()
research_funding_project.skills_list.add(r_skill, machine_learning_skill, ggplot2_library_skill)
research_funding_project.save()

#https://github.com/rowanv/pred-res-fund
#http://www.totiusmundi.com/QuantPortfolio/QuantPortfolio.html')


energy_industry_prediction_project = Project(title='Energy Industry Development Prediction',
	description = 'Used R to predict the development of the energy industry using'
	'a patent dataset. Determined whether certain technologies had reached a '
	'saturation point.',
	link='porfolio/energy_industry_prediction/',
	thumbnail='/static/images/abstract_green.png',
	tag_name='energy_industry_prediction')
energy_industry_prediction_project.save()
energy_industry_prediction_project.skills_list.add(r_skill, ggplot2_library_skill)
energy_industry_prediction_project.save()

inclusion_with_identity_project = Project(title='Inclusion with Identity Dashboard',
	description = 'Created an online, interactive Tableau dashboard for the Inter-American'
	'Development Bank that visualized development indicators across various races'
	'and ethnicities in Latin America. Scraped national census data to create'
	'database that populated the dashboard.',
	link='portfolio/inclusion_with_identity/',
	thumbnail='/static/images/inclusion_with_identity_pic.png',
	tag_name='inclusion_with_identity')
inclusion_with_identity_project.save()
inclusion_with_identity_project.skills_list.add(r_skill, tableau_skill)
inclusion_with_identity_project.save()

social_media_dashboard_project = Project(title='Social Media Dashboard',
	description = 'Created a real-time, dynamically updating social media dashboard that '
	'tracks a Twitter account\'s key use statistics.',
	link='porfolio/social_media_dashboard/',
	thumbnail='/static/images/abstract_green.png',
	tag_name='social_media_dashboard')
social_media_dashboard_project.save()
social_media_dashboard_project.skills_list.add(python_skill, bokeh_library_skill, pandas_library_skill)
social_media_dashboard_project.save()



