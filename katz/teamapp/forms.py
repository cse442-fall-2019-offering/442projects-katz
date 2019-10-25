from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django.forms import ModelForm

from teamapp.models import Team
class createTeam(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['team_info'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['max_teammates'].widget.attrs.update({'class': 'form-control form-control-lg'})
    
    def clean_max_teammates(self):
        data = self.cleaned_data['max_teammates']
        if data < 1:
            raise ValidationError(_('Invalid number of teammates - must be at lease 1'))

        return data

    class Meta:
        model = Team
        fields = ['name','team_info','max_teammates',]

from teamapp.models import Student
from django.contrib.auth.models import User
class createAccountForm(ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','password',]