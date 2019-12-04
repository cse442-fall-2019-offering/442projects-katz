from django.shortcuts import render
from teamapp.models import School, EmailURL, Class, Team, Student, EnrolledIn, Teams
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from teamapp.forms import createTeam, UserForm, StudentForm , PasswordChangeFormCSS
from django.contrib.auth import update_session_auth_hash


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

@login_required
def classpage(request, idOfClass):
    students = EnrolledIn.objects.all().filter(in_class__id = idOfClass)
    teams = Team.objects.all().filter(in_class__id__exact = idOfClass)
    currStudent = Student.objects.get(account_id = request.user.id)
    isStudent = EnrolledIn.objects.all().filter(in_class__id = idOfClass, student_id = currStudent.id)
    classOfId = Class.objects.all().get(id = idOfClass)

    if request.method == 'POST' and isStudent.exists():
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

    joined = students.filter(student__account = request.user).exists()

    context = {
        'teams' : teams,
        'students' : students,
        'classOfId' : classOfId,
        'form' : form,
        'joined' : joined,
    }

    return render(request, 'classpage.html', context=context)

@login_required
def teampage(request, idOfTeam):
    team = Team.objects.get(id=idOfTeam)
    teamMems = Teams.objects.all().filter(team__id = idOfTeam)
    userteam = teamMems.filter(student__account = request.user)

    if request.method == 'POST' and team.team_leader.account == request.user:
        form = createTeam(request.POST)
        if form.is_valid():
            team.name = form.cleaned_data['name']
            team.team_info = form.cleaned_data['team_info']
            team.max_teammates = form.cleaned_data['max_teammates']
            team.save()
            
            return HttpResponseRedirect(reverse('teampage',args=[str(team.id)]))
    else:
        teamName = team.name
        descrip = team.team_info
        maxteam = team.max_teammates
        form = createTeam(initial={'name': teamName, 'team_info':descrip, 'max_teammates':maxteam})

    context = {
        'form' : form,
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

from teamapp.forms import createAccountForm
from django.contrib.auth.forms import UserCreationForm
def createAccount(request):
    form = UserCreationForm()
    context = {
        'form' : form,
    }

    #return render(request, 'profilepage.html', context=context)
    return render(request, 'createaccount.html', context=context)

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

@login_required
def teampageEdit(request, idOfTeam):
    team = Team.objects.get(id = idOfTeam)

    if request.method == 'POST':
        form = createTeam(request.POST)
        if form.is_valid():
            team.name = form.cleaned_data['name']
            team.team_info = form.cleaned_data['team_info']
            team.max_teammates = form.cleaned_data['max_teammates']
            team.save()

            return HttpResponseRedirect(reverse('teampage',args=[str(team.id)]))
    else:
        teamName = team.name
        descrip = team.team_info
        maxteam = team.max_teammates
        form = createTeam(initial={'name': teamName, 'team_info':descrip, 'max_teammates':maxteam})

    context = {
        'form' : form,
        'team' : team,
    }

    return render(request, 'editteam.html', context=context)

@login_required
def profileEdit(request):
    loggedInUser = request.user
    student = Student.objects.get(account = loggedInUser);

    if request.method == 'POST':
        userform = UserForm(request.POST)
        studform = StudentForm(request.POST)
        if userform.is_valid() and studform.is_valid():
            student.account.first_name = userform.cleaned_data['first_name']
            student.account.last_name = userform.cleaned_data['last_name']
            student.middle_name = studform.cleaned_data['middle_name']
            student.account.save()
            student.save()

            return HttpResponseRedirect(reverse('myprofilepage'))
    else:
        firstname = loggedInUser.first_name
        lastname = loggedInUser.last_name
        middlename = student.middle_name

        userform = UserForm(initial={'first_name': firstname, 'last_name':lastname})
        studform = StudentForm(initial={'middle_name': middlename})

    context = {
        'userform' : userform,
        'studform' : studform,
    }

    return render(request, 'editprofile.html', context=context)

@login_required
def changePassword(request):
    loggedInUser = request.user
    if request.method == 'POST':
        form = PasswordChangeFormCSS(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)

            return HttpResponseRedirect(reverse('myprofilepage'))

    else:
        form = PasswordChangeFormCSS(request.user)

    context = {
        'form' : form,
    }

    return render(request, 'changepassword.html', context)

@login_required
def schoolClasses(request):
    loggedInUser = request.user
    student = Student.objects.get(account = loggedInUser)
    classes = Class.objects.all().filter(school = student.school).order_by('name', 'start_time', 'professor_name')

    context = {
        'classes' : classes,
    }

    return render(request, 'schoolclasses.html', context=context)

@login_required
def joinClass(request, idOfClass):
    s = Student.objects.get(account = request.user)
    c = Class.objects.get(id = idOfClass);

    if request.method == 'POST':
        joinClassInstance = EnrolledIn(student = s, in_class = c)
        try:
            joinClassInstance.save()
        except Exception:
            pass

    return HttpResponseRedirect(reverse('classpage', args=[str(c.id)]))

@login_required
def leaveClass(request, idOfClass):
    s = Student.objects.get(account = request.user)
    c = Class.objects.get(id = idOfClass);

    if request.method == 'POST':
        joinClassInstance = EnrolledIn.objects.get(student = s, in_class = c)
        try:
            joinClassInstance.delete()
        except Exception:
            pass

    return HttpResponseRedirect(reverse('classpage', args=[str(c.id)]))
