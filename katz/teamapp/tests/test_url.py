from django.test import SimpleTestCase
from django.urls import reverse, resolve
from teamapp.views import homepage, classpage

class TestUrls(SimpleTestCase):

    #tests the homepage url if it routing to its function
    def test_homepage_url(self):
        print("tests the homepage url if it routing to its function")
        url = reverse('homepage')
        self.assertEquals(resolve(url).func, homepage)

    #tests the homepage url if it routing to its function with class id 3
    def test_classpage_url(self):
        print("tests the homepage url if it routing to its function with class id 3")
        url = reverse('classpage', args=['3'])
        self.assertEquals(resolve(url).func, classpage)
