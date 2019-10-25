from django.shortcuts import render
from teamapp.models import School, EmailURL, Class, Team, Student, EnrolledIn, Teams

# Create your views here.
def homepage(request):
    classes = EnrolledIn.objects.all().filter(student__account__username__exact = 'igorkuzm')
    teams = Teams.objects.all().filter(student__account__username__exact = 'igorkuzm')

    context = {
        'classes' : classes,
        'teams' : teams,
    }

    return render(request, 'homepage.html', context=context)

def classpage(request, idOfClass):
    teams = Team.objects.all().filter(in_class__id__exact = idOfClass)
    students = EnrolledIn.objects.all().filter(in_class__id = idOfClass)
    classOfId = Class.objects.all().get(id = idOfClass)

    context = {
        'teams' : teams,
        'students' : students,
        'classOfId' : classOfId,
    }

    return render(request, 'classpage.html', context=context)