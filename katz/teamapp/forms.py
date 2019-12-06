from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from teamapp.models import Team

#Form used to create team input functionality
class createTeam(ModelForm):
    #What fields get updated
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control '})
        self.fields['team_info'].widget.attrs.update({'class': 'form-control '})
        self.fields['max_teammates'].widget.attrs.update({'class': 'form-control '})

    def clean_max_teammates(self):
        data = self.cleaned_data['max_teammates']
        if data < 1:
            raise ValidationError(_('Invalid number of teammates - must be at lease 1'))

        return data

    class Meta:
        model = Team
        #Fields the form takes
        fields = ['name','team_info','max_teammates', 'team_image']


from teamapp.models import Student
from django.contrib.auth.models import User
#create account form which produces the create accunt form
class createAccountForm(ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','password',]

class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control '})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control '})

    class Meta:
        model = User
        fields = ['first_name', 'last_name',]

#student form the produces the fields named for forms.
class StudentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['middle_name'].widget.attrs.update({'class': 'form-control '})

    class Meta:
        model = Student
        fields = ['middle_name', 'student_image']

from django.forms.utils import ErrorList
#produces an error form when error occurs
class CustomErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return ''
        return '<div class="alert alert-danger">%s</div>' % ''.join(['<div class="error">%s</div>' % e for e in self])

from django.contrib.auth.forms import PasswordChangeForm
#checks if password is authenticated
class PasswordChangeFormCSS(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control '})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control '})
        self.fields['old_password'].widget.attrs.update({'class': 'form-control '})
        self.error_class = CustomErrorList
