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

    #Max teammates function to check if its at least 1
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
class createAccountForm(ModelForm):

    class Meta:
        model = User
        #Create Account form with the fields that it displays
        fields = ['first_name', 'last_name', 'username','password',]
