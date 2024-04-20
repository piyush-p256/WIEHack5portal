from django import forms
from .models import Round1,Round2, Round3

class Round1Form(forms.ModelForm):
    class Meta:
        model = Round1
        fields = ['team_no','team_name','mode', 'member_name', 'member2', 'member3', 'member4', 'ppt_link']

class Round2UploadForm(forms.ModelForm):
    class Meta:
        model = Round2
        fields = ['team_no', 'team_name', 'mode', 'member_name','member2', 'member3', 'member4', 'youtube_link', 'github_link2','ppt_link2']


class Round3UploadForm(forms.ModelForm):
    class Meta:
        model = Round3
        fields = ['team_no', 'team_name', 'mode', 'member_name', 'member2', 'member3', 'member4', 'youtube_link3', 'github_link3', 'ppt3_link']
