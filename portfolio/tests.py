from django.test import TestCase
from django.core.urlresolvers import resolve
from django.core.exceptions import ValidationError

from portfolio.views import portfolio
from portfolio.models import Project


class PortfolioPageTest(TestCase):

	def test_portfolio_url_resolves_to_portfolio_page_view(self):
		found = resolve('/portfolio/')
		self.assertEqual(found.func, portfolio)


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
