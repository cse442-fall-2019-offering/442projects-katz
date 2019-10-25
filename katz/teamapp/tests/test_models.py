from django.test import TestCase, Client
from django.urls import reverse
from teamapp.models import School, Class, EmailURL, Team, Student, EnrolledIn, Teams
from django.contrib.auth.models import User
import json

class TestModels(TestCase):

    #Holds the create client that is used on all other test cases
    def setUp(self):
        self.user1 = User.objects.create(username = "user", first_name = "hello", last_name = "there")
        self.school1 = School.objects.create(name="real school")
        self.emailurl1 = EmailURL.objects.create(URL="realschool@not.edu", school = self.school1)
        self.class1 = Class.objects.create(name ="CSE442", school = self.school1, professor_name = "Matthew Hurts", class_info = "a", start_time = "02:01", end_time = "03:01")
        self.team1 = Team.objects.create(in_class = self.class1, name = 'team katz', team_info = 'a', max_teammates = '3')
        self.student1 = Student.objects.create(account = self.user1, school = self.school1, middle_name = "q")
        self.enrolledin1 = EnrolledIn(student = self.student1, in_class = self.class1)
        self.teams1 = Teams(student = self.student1, team = self.team1)

    #Tests if school model
    def test_school_return(self):
        self.assertEquals(str(self.school1), 'real school')

    #Tests if EmaiURL model
    def test_emailurl_return(self):
        self.assertEquals(str(self.emailurl1), 'realschool@not.edu')

    #Tests if class model
    def test_class_return(self):
        self.assertEquals(str(self.class1), 'CSE442 real school')
        self.assertEquals(self.class1.get_absolute_url(), '/home/1/')

    #Tests if team model
    def test_team_return(self):
        self.assertEquals(str(self.team1), 'team katz')

    #Tests if student model
    def test_student_return(self):
        self.assertEquals(str(self.student1), 'hello q there')

    #Tests if EnrolledIn model
    def test_enrolledin_return(self):
        self.assertEquals(str(self.enrolledin1), 'hello there - CSE442')

    #Tests if teams model
    def test_teams_return(self):
        self.assertEquals(str(self.teams1), 'hello q there - team katz')
