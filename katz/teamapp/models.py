from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class School(models.Model):
    name = models.CharField(primary_key=True, max_length=255,help_text='Enter school_name',unique=True)

    def __str__(self):
        return self.name

class EmailURL(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    URL = models.URLField(primary_key=True, max_length=255,help_text='Enter school email url',unique=True)

    def __str__(self):
        return self.URL

class Class(models.Model):
    name = models.CharField(max_length=255,help_text='Enter class name')
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
    professor_name = models.CharField(max_length=255,help_text='Enter professor name')
    class_info = models.TextField()

    def __str__(self):
        return self.name + " " + self.school.name

    class Meta:
        unique_together = (("name","school","start_time","end_time","professor_name"),)

    def get_absolute_url(self):
        return reverse('classpage', args=[str(self.id)])


class Student(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=255, null=False, blank=True, default="")
    
    def __str__(self):
        return self.account.first_name + " " + self.middle_name + " " + self.account.last_name

    def get_absolute_url(self):
        return reverse('profilepage',args=[str(self.account.username)])

class Team(models.Model):
    in_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    team_info = models.TextField()
    max_teammates = models.IntegerField(null=False, blank=False)
    team_leader = models.ForeignKey('Student', null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("in_class","name"),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('teampage', args=[str(self.id)])


class EnrolledIn(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    in_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("student","in_class"),)

    def __str__(self):
        return self.student.account.first_name +" "+self.student.account.last_name + " - " + self.in_class.name

class Teams(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("student","team"),)

    def __str__(self):
        return self.student.__str__() + " - " + self.team.name


