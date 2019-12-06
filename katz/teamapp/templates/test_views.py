from django.test import TestCase, Client
from django.urls import reverse
from teamapp.models import School, EmailURL, Team, Student, EnrolledIn, Teams
import json

class TestViews(TestCase):

    #Holds the create client that is used on all other test cases
    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('homepage')
        self.classpage_url = reverse('homepage')

    #tests if the homepage function acceses the template
    def test_homepage_GET(self):
        print("Tests if homepage function acceses the template")
        response = self.client.get(self.homepage_url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'homepage.html')

    #tests if the classpage function acceses the template
    def test_classpage_GET(self):
        print("Tests if classpage function acceses the template")
        response = self.client.get(self.classpage_url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'homepage.html')
