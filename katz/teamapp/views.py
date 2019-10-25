from django.shortcuts import render
from teamapp.models import School, EmailURL, Class, Team, Student, EnrolledIn, Teams
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

@login_required
def homepage(request):

    user = request.user.username
    classes = EnrolledIn.objects.all().filter(student__account__username__exact = user)
    teams = Teams.objects.all().filter(student__account__username__exact = user)

    context = {
        'classes' : classes,
        'teams' : teams,
    }

    return render(request, 'homepage.html', context=context)

from teamapp.forms import createTeam

@login_required
def classpage(request, idOfClass):
    teams = Team.objects.all().filter(in_class__id__exact = idOfClass)
    students = EnrolledIn.objects.all().filter(in_class__id = idOfClass)
    classOfId = Class.objects.all().get(id = idOfClass)

    if request.method == 'POST':
        form = createTeam(request.POST)
        if form.is_valid():
            newteam = Team()
            newteam.in_class = Class.objects.get(id = idOfClass)
            newteam.name = form.cleaned_data['name']
            newteam.team_info = form.cleaned_data['team_info']
            newteam.max_teammates = form.cleaned_data['max_teammates']
            newteam.save()
            return HttpResponseRedirect(reverse('classpage',args=[str(idOfClass)]))
    else:
        form = createTeam()

    context = {
        'teams' : teams,
        'students' : students,
        'classOfId' : classOfId,
        'form' : form,
    }

    return render(request, 'classpage.html', context=context)

@login_required
def teampage(request, idOfTeam):
    team = Team.objects.get(id=idOfTeam)
    teamMems = Teams.objects.all().filter(team__id = idOfTeam)
    userteam = teamMems.filter(student__account = request.user)

    context = {
        'team' : team,
        'teamMems' : teamMems,
        'idOfTeam' : idOfTeam,
        'userteam' : userteam,
     }

    return render(request, 'teampage.html', context=context)

@login_required
def profilepage(request, usrname):

    student = Student.objects.get(account__username = usrname)
    teams = Teams.objects.all().filter(student__account__username = usrname)

    context = {
        'student' : student,
        'teams' : teams,
    }
    return render(request, 'profilepage.html', context=context)

@login_required
def jointeam(request, idOfTeam):
    s = Student.objects.get(account = request.user)
    t = Team.objects.get(id=idOfTeam)

    joinTeamInstance = Teams(student = s, team = t)
    
    try:
        joinTeamInstance.save()
    except Exception:
        pass

    return HttpResponseRedirect(reverse('teampage', args=[str(idOfTeam)]))

@login_required
def leaveteam(request, idOfTeam):
    t = Teams.objects.all().filter(team__id = idOfTeam)
    course = Team.objects.get(id = idOfTeam)
    instance = t.filter(student__account = request.user)

    if instance:
        try:
            instance.delete()
        except Exception:
            pass
    
    if Teams.objects.all().filter(team__id = idOfTeam):
        pass
    else:
        Team.objects.get(id = idOfTeam).delete()
        return HttpResponseRedirect(reverse('classpage', args=[str(course.in_class.id)]))
    
    return HttpResponseRedirect(reverse('teampage', args=[str(idOfTeam)]))

@login_required
def myprofilepage(request):
    return HttpResponseRedirect(reverse('profilepage', args=[str(request.user.username)]))