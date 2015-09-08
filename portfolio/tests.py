from django.test import TestCase
from django.core.urlresolvers import resolve

from portfolio.views import portfolio


class PortfolioPageTest(TestCase):

	def test_portfolio_url_resolves_to_portfolio_page_view(self):
		found = resolve('/portfolio/')
		self.assertEqual(found.func, portfolio)

