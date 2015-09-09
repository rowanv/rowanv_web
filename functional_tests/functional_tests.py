from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_view_a_portfolio_entry(self):
        # Come to check out portfolio home page
        self.browser.get('http://localhost:8000/portfolio/')

        #see that the title mentiosn portfolio
        self.assertIn('Portfolio', self.browser.title)



    def test_layout_and_styling(self):
        self.browser.get('http://localhost:8000/portfolio/')
        self.browser.set_window_size(1024, 768)
        
        #there is a nav bar at the top
        navbar = self.browser.find_element_by_tag_name('nav') 

        #and it is black-ish grey!
        self.assertEqual(navbar.value_of_css_property('color'), 'rgba(51, 51, 51, 1)')
