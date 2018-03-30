'''
To run unit tests:
python3 manage.py test portfolio
'''


from django.test import TestCase
from django.core.urlresolvers import resolve
from django.core.exceptions import ValidationError

import portfolio.views as views
from portfolio.models import Project, PastWorkEngagement


class PageViewTest(TestCase):

    def test_portfolio_url_resolves_to_portfolio_page_view(self):
        found = resolve('/portfolio/')
        self.assertEqual(found.func, views.portfolio)

    def test_about_url_resolves_to_about_page_view(self):
        found = resolve('/portfolio/about/')
        self.assertEqual(found.func, views.about)

    def test_resume_url_resolves_to_resume_view(self):
        found = resolve('/portfolio/resume/')
        self.assertEqual(found.func, views.resume)


class ProjectModelTest(TestCase):

    def test_default_current_project(self):
        project = Project()
        self.assertEqual(project.current_project, False)

    def test_cannot_save_empty_projects(self):
        project = Project(title='', description='', link='')
        with self.assertRaises(ValidationError):
            project.save()
            project.full_clean()

    def test_tags_are_related_to_projects(self):
        pass


class ServicesViewTest(TestCase):

    def setUp(self):
        engagement = PastWorkEngagement(description='a past work description')
        engagement.full_clean()
        engagement.save()

    def test_can_view_services_in_services_view(self):
        response = self.client.get('/portfolio/services/')
        self.assertContains(response, 'a past work description')
