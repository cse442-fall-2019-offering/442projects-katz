from django.shortcuts import render
from teamapp.models import School, EmailURL, Class, Team, Student, EnrolledIn, Teams
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse


# Returns the homepage for the specific logged in user
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

# Returns the classpage for a specific class that was requested
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
            newteam.team_leader = Student.objects.get(account = request.user)
            newteam.save()

            leaderentry = Teams();
            leaderentry.student = Student.objects.get(account = request.user)
            leaderentry.team = newteam
            leaderentry.save()

            return HttpResponseRedirect(reverse('teampage',args=[str(newteam.id)]))
    else:
        form = createTeam()

    context = {
        'teams' : teams,
        'students' : students,
        'classOfId' : classOfId,
        'form' : form,
    }

    return render(request, 'classpage.html', context=context)

# Returns the teampage for a specific team that was requested
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

# Returns the user profile for a specific user that was requested
@login_required
def profilepage(request, usrname):

    student = Student.objects.get(account__username = usrname)
    teams = Teams.objects.all().filter(student__account__username = usrname)

    context = {
        'student' : student,
        'teams' : teams,
    }
    return render(request, 'profilepage.html', context=context)

# Adds student to a specific team when its called
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

# Leaves a team when this fuction is called
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

# Displays the logged in user profile page
@login_required
def myprofilepage(request):
    return HttpResponseRedirect(reverse('profilepage', args=[str(request.user.username)]))

from teamapp.forms import createAccountForm
from django.contrib.auth.forms import UserCreationForm

# Displays the create account pages
def createAccount(request):
    form = UserCreationForm()
    context = {
        'form' : form,
    }

    return render(request, 'createaccount.html', context=context)

# kicks a member if user is team leader, when given a team id, and username
@login_required
def kickMember(request, idOfTeam, usr):
    t = Teams.objects.all().filter(team__id = idOfTeam)
    course = Team.objects.get(id = idOfTeam)
    instance = t.filter(student__account__username = usr)
    team = Team.objects.get(id = idOfTeam)

    if team.team_leader.account == request.user:
        if instance:
            try:
                instance.delete()
            except Exception:
                pass

    return HttpResponseRedirect(reverse('teampage', args=[str(idOfTeam)]))

# Displays the edit team page when called with a team id
@login_required
def teampageEdit(request, idOfTeam):
    team = Team.objects.get(id = idOfTeam)

    if request.method == 'POST':
        form = createTeam(request.POST, request.FILES)
        if form.is_valid():
            team.name = form.cleaned_data['name']
            team.team_info = form.cleaned_data['team_info']
            team.max_teammates = form.cleaned_data['max_teammates']
            team.team_image = form.cleaned_data['team_image']
            team.save()

            return HttpResponseRedirect(reverse('teampage',args=[str(team.id)]))
    else:
        teamName = team.name
        descrip = team.team_info
        maxteam = team.max_teammates
        teamimage = team.team_image
        form = createTeam(initial={'name': teamName, 'team_info':descrip, 'max_teammates':maxteam, 'team_image':teamimage})

    context = {
        'form' : form,
        'team' : team,
    }

    return render(request, 'editteam.html', context=context)
