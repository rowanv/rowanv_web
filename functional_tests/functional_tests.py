import sys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_view_a_portfolio_entry(self):
        # Come to check out portfolio home page
        self.browser.get(self.server_url + '/portfolio/')

        # see that the title mentiosn portfolio
        self.assertIn('Portfolio', self.browser.title)

    def test_layout_and_styling(self):
        self.browser.get(self.server_url + '/portfolio/')
        self.browser.set_window_size(1024, 768)

        # there is a nav bar at the top
        navbar = self.browser.find_element_by_tag_name('nav')

        # and it is black-ish grey!
        self.assertEqual(navbar.value_of_css_property(
            'color'), 'rgba(51, 51, 51, 1)')
