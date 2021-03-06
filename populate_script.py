from portfolio.models import Skill, Project, PastWorkEngagement


# Past Work Engagements
past_engagement_descriptions = [
    ('Architected a scalable, distributed Big Data system for an early-stage '
     'startup in the AWS cloud'),
    ('Increased the efficiency of a Big Data pipeline by using machine '
     'learning to automate anomaly detection'),
    ('Greatly improved the efficiency of a startup\'s analytics queries by '
     'architecting and migrating a data warehouse solution that leveraged '
     'Amazon Redshift'),
    ('Enabled a company to answer oversight and compliance-related questions '
     'by undertaking a custom Data Science analysis of access logs as part of '
     'an auditing process'),
    ('Enabled a company to deliver a valuable visual analytics solution to their'
     'clients by architecting and building out a cloud-based data architecture '
     'and consumer-facing dashboard solution for a mid-size company.'),
]

for description in past_engagement_descriptions:
    past_engagement, _ = PastWorkEngagement.objects.get_or_create(description=description)
    past_engagement.full_clean()
    past_engagement.save()


# Skills

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

data_science_skill = Skill(name='Data Science')
data_science_skill.save()

statistics_skill = Skill(name='Statistics')
statistics_skill.save()

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

java_script_skill = Skill(name='JavaScript')
java_script_skill.save()

d3_library_skill = Skill(name='d3 Library')
d3_library_skill.save()

matplotlib_library_skill = Skill(name='matplotlib Library')
matplotlib_library_skill.save()

geo_map_skill = Skill(name='Geomaps')
geo_map_skill.save()

django_library_skill = Skill(name='Django Library')
django_library_skill.save()

flask_library_skill = Skill(name='Flask Library')
flask_library_skill.save()

mysql_database_skill = Skill(name='MySQL Database')
mysql_database_skill.save()

html_skill = Skill(name='HTML')
html_skill.save()

css_skill = Skill(name='CSS')
css_skill.save()

ajax_skill = Skill(name='Ajax')
ajax_skill.save()

sparklines_dash_project = Project(
    title='Real-Time Sparklines Dashboard',
    description='A real-time dashboard for quickly visualizing tends in currency '
    'fluctuations for major currencies over the past month. Developed end-to-end '
    'to display metrics in real-time. Extracts metrics from the ECB currency '
    'API, transforms data using Python\'s Pandas, visualizes sparklines using '
    'd3. Served using nginx and gunicorn via the Flask micro-framework.',
    link='http://sparklines-dash.rowanv.com',
    thumbnail='/static/images/sparklines_dash.png',
    tag_name='sparklines_dash',
    code_link='https://github.com/rowanv/sparklines_dash')
sparklines_dash_project.save()
sparklines_dash_project.skills_list.add(
    python_skill,
    pandas_library_skill,
    flask_library_skill,
    java_script_skill,
    d3_library_skill,
    html_skill,
    css_skill)

business_dash_project = Project(
    title='Real-Time Business Dashboard',
    description='  A dynamic dashboard for visualizing a movie rental company'
    '\'s key business metrics. Developed end-to-end to display metrics in real-time.'
    'Extracts metrics from a MySQL database, transforms data using Python, '
    'visualizes charts and graphs using d3. Served using nginx and gunicorn '
    'via the Flask micro-framework.',
    link='http://dash.rowanv.com',
    thumbnail='/static/images/business_dash.png',
    tag_name='business_dash',
    code_link='https://github.com/rowanv/giraffe_dash')
business_dash_project.save()
business_dash_project.skills_list.add(
    python_skill,
    pandas_library_skill,
    flask_library_skill,
    mysql_database_skill,
    java_script_skill,
    html_skill,
    css_skill,
    d3_library_skill)
business_dash_project.save()

oecd_project = Project(
    title='OECD Unemployment Visualization',
    description='A dynamic visualization of the unemployment rates in OECD countries over the past 15 years.',
    link='/portfolio/oecd_unemployment/',
    thumbnail='/static/images/oecd_unemployment_pic.png',
    tag_name='oecd',
    code_link='https://github.com/rowanv/giraffe_viz/blob/master/oecd_unemployment.py')
oecd_project.save()
oecd_project.skills_list.add(
    python_skill,
    pandas_library_skill,
    bokeh_library_skill)
oecd_project.save()

voter_turnout_project = Project(
    title='Voter Turnout Visualization',
    description='A dynamic visualization of presidential voter turnout by country'
    ' over time.',
    link='/portfolio/voter_turnout/',
    thumbnail='/static/images/voter_turnout_pic.png',
    tag_name='voter_turnout',
    code_link='https://github.com/rowanv/giraffe_viz/tree/master/voter_turnout')
voter_turnout_project.save()
voter_turnout_project.skills_list.add(
    java_script_skill,
    d3_library_skill,
    python_skill,
    pandas_library_skill,
    matplotlib_library_skill)
voter_turnout_project.save()

finders_keepers_project = Project(
    title='Finders Keepers App',
    description='A Django-based application that leverages the Google'
    ' Maps API to determine wheter a clicked-on location has an '
    'address or not.',
    link='http://finderskeepers.rowanv.com/',
    thumbnail='/static/images/finders_keepers.png',
    tag_name='finders_keepers',
    code_link='https://github.com/rowanv/finders_keepers')
finders_keepers_project.save()
finders_keepers_project.skills_list.add(
    java_script_skill,
    python_skill,
    django_library_skill,
    ajax_skill)
finders_keepers_project.save()

gender_olympics_project = Project(
    title='Gender and the Olympics Visualization',
    description='A dynamic visualization of the medal count for the Olympic Games'
    ' by gender over time.',
    link='/portfolio/gender_olympics/',
    thumbnail='/static/images/gender_olympics_pic.png',
    tag_name='gender_olympics',
    code_link='https://github.com/rowanv/giraffe_viz/blob/master/olympics/olympics_medal_line_graph_viz.html')
gender_olympics_project.save()
gender_olympics_project.skills_list.add(
    java_script_skill,
    d3_library_skill,
    python_skill,
    pandas_library_skill,
    matplotlib_library_skill)
gender_olympics_project.save()

ith_degree_search_project = Project(
    title='Big Data Ith Degree Connections Finder',
    description='A Pig and Bash tool to find ith-degree connections for a list of '
    '1st-degree connections between nodes. This tool uses a Pig abstraction layer '
    'to create Map Reduce jobs that allow for scaling to a very large number '
    'of connections.',
    thumbnail='/static/images/ith_degree_search_pic.png',
    link='https://github.com/rowanv/ith_degree_search',
    tag_name='ith_degree_search',
    code_link='https://github.com/rowanv/ith_degree_search')
ith_degree_search_project.save()
ith_degree_search_project.skills_list.add(
    pig_skill, bash_skill, map_reduce_skill, hadoop_skill)
ith_degree_search_project.save()


windchill_project = Project(
    title='Windchill Visualization',
    description='A dynamic, visual representation of the Siple windchill formula.',
    link='/portfolio/windchill/',
    thumbnail='/static/images/windchill_pic.png',
    tag_name='windchill',
    code_link='https://github.com/rowanv/giraffe_viz/blob/master/windchill.py')
windchill_project.save()
windchill_project.skills_list.add(
    python_skill,
    pandas_library_skill,
    bokeh_library_skill,
    numpy_library_skill)
windchill_project.save()


electronegativity_project = Project(
    title='Electronegativity Table',
    description='A dynamic representation of Periodic Table electronegativities.',
    link='/portfolio/electronegativity/',
    thumbnail='/static/images/electronegativity_pic.png',
    tag_name='electronegativity',
    code_link='https://github.com/rowanv/data-science/blob/master/Visualizations/electronegativity_table.py')
electronegativity_project.save()
electronegativity_project.skills_list.add(python_skill, bokeh_library_skill)
electronegativity_project.save()

geo_twitter_project = Project(
    title='Geo-Based Offline Sales Research',
    description='Project undertaken at Twitter to determine the offline '
    'sales impact of social networking platforms using a Geo-Based Methodology. '
    'Presented at QCon and Grace Hopper.',
    link='/portfolio/geo_twitter/',
    thumbnail='/static/images/abstract_green.png',
    tag_name='geo_twitter')
geo_twitter_project.save()
geo_twitter_project.skills_list.add(
    python_skill,
    r_skill,
    pandas_library_skill,
    bash_skill,
    pig_skill,
    hadoop_skill,
    data_science_skill,
    statistics_skill,
    geo_map_skill)
geo_twitter_project.save()

brazil_map_project = Project(
    title='Brazil Map',
    description='A map of Brazil showing major cities, created using JavaScript\'s d3.js'
    'library',
    link='/portfolio/brazil_map/',
    thumbnail='/static/images/brazil_map_pic.png',
    tag_name='brazil_map',
    code_link='https://github.com/rowanv/giraffe_viz/blob/master/mapping/brazil_map.html')
brazil_map_project.save()
brazil_map_project.skills_list.add(d3_library_skill, geo_map_skill)
brazil_map_project.save()

housing_prices_project = Project(
    title='Housing Prices Linear Regression',
    description='A simple, dynamic data visualization using Python\'s Pandas and Bokeh libraries.',
    link='/portfolio/housing_prices/',
    thumbnail='/static/images/linear_regression_pic.png',
    tag_name='housing_prices',
    code_link='https://github.com/rowanv/giraffe_viz/blob/master/housing_prices.py')
housing_prices_project.save()
housing_prices_project.skills_list.add(python_skill, bokeh_library_skill,
                                       statistics_skill)
housing_prices_project.save()

research_funding_project = Project(
    title='Research Funding Predictions Project',
    description='I explore the following research question: "What determines the levels of'
    'funding that an NSF or NASA-funded project receives?".'
    #'I define high levels of research'
    #'funding as the upper decile for the original, raw funding variable. I then use text '
    #'analytics to determine the words in the abstract that were correlated'
    #'with high levels of funding.
    'Using CART, logistic regression, and Random Forest models,'
    'I am able to predict whether a research project is likely to have received high levels of funding'
    'with around 90% accuracy.',
    link='https://github.com/rowanv/pred-res-fund',
    thumbnail='/static/images/research_funding_pic.png',
    tag_name='research_funding',
    code_link='https://github.com/rowanv/pred-res-fund')
research_funding_project.save()
research_funding_project.skills_list.add(
    r_skill,
    machine_learning_skill,
    ggplot2_library_skill,
    data_science_skill,
    statistics_skill)
research_funding_project.save()

# https://github.com/rowanv/pred-res-fund
# http://www.totiusmundi.com/QuantPortfolio/QuantPortfolio.html')


energy_industry_prediction_project = Project(title='Energy Industry Development Prediction',
                                             description='Used R to predict the development of the energy industry using'
                                             'a patent dataset. Determined whether certain technologies had reached a '
                                             'saturation point.',
                                             # link='porfolio/energy_industry_prediction/',
                                             thumbnail='/static/images/abstract_green.png',
                                             tag_name='energy_industry_prediction'
                                             )
energy_industry_prediction_project.save()
energy_industry_prediction_project.skills_list.add(
    r_skill,
    ggplot2_library_skill,
    data_science_skill,
    statistics_skill,
    machine_learning_skill)
energy_industry_prediction_project.save()

inclusion_with_identity_project = Project(title='Inclusion with Identity Dashboard',
                                          description='Created an online, interactive Tableau dashboard for the Inter-American'
                                          'Development Bank that visualized development indicators across various races'
                                          'and ethnicities in Latin America. Scraped national census data to create'
                                          'database that populated the dashboard.',
                                          # link='portfolio/inclusion_with_identity/',
                                          thumbnail='/static/images/inclusion_with_identity_pic.png',
                                          tag_name='inclusion_with_identity')
inclusion_with_identity_project.save()
inclusion_with_identity_project.skills_list.add(
    r_skill, tableau_skill, data_science_skill, geo_map_skill)
inclusion_with_identity_project.save()

social_media_dashboard_project = Project(title='Social Media Dashboard',
                                         description='Created a real-time, dynamically updating social media dashboard that '
                                         'tracks a Twitter account\'s key use statistics.',
                                         # link='porfolio/social_media_dashboard/',
                                         thumbnail='/static/images/abstract_green.png',
                                         tag_name='social_media_dashboard')
social_media_dashboard_project.save()
social_media_dashboard_project.skills_list.add(
    python_skill,
    bokeh_library_skill,
    pandas_library_skill,
    data_science_skill)
social_media_dashboard_project.save()

# Also added AWS Architecture Visualization
