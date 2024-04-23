from django.db import models

class Team(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    team_no = models.IntegerField(unique=True)
    round_no = models.IntegerField(default=0)
    mode = models.CharField(max_length=50, default='online')
    team_name = models.CharField(max_length=255)
    team_leader = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Team {self.team_no}"

class Round1(models.Model):
    team_no = models.IntegerField(unique=True)
    team_name = models.CharField(max_length=255)
    mode = models.CharField(max_length=50)
    member_name = models.CharField(max_length=255, blank=True, null=True) 
    member2 = models.CharField(max_length=255, blank=True, null=True)
    member3 = models.CharField(max_length=255, blank=True, null=True)
    member4 = models.CharField(max_length=255, blank=True, null=True)
    ppt_link = models.URLField(blank=True)

    def __str__(self):
        return f"Round 1 - Team {self.team_no}"
    
class Round2(models.Model): 
    team_email = models.EmailField(unique=True, blank=True)   
    team_no = models.IntegerField(unique=True)
    team_name = models.CharField(max_length=255)
    mode = models.CharField(max_length=50)
    member_name = models.CharField(max_length=255, blank=True, null=True) 
    member2 = models.CharField(max_length=255, blank=True, null=True)
    member3 = models.CharField(max_length=255, blank=True, null=True)
    member4 = models.CharField(max_length=255, blank=True, null=True)
    youtube_link = models.URLField(max_length=255, blank=True, null=True) 
    github_link2 = models.URLField(max_length=255)
    ppt_link2 = models.URLField(blank=True)

    def __str__(self):
        return f"Round 2 - Team {self.team_no}"


class Round3(models.Model): 
    team_email = models.EmailField(unique=True, blank=True)
    team_no = models.IntegerField(unique=True)
    team_name = models.CharField(max_length=255)
    mode = models.CharField(max_length=50)
    member_name = models.CharField(max_length=255, blank=True, null=True) 
    member2 = models.CharField(max_length=255, blank=True, null=True)
    member3 = models.CharField(max_length=255, blank=True, null=True)
    member4 = models.CharField(max_length=255, blank=True, null=True)
    youtube_link3 = models.URLField(max_length=255, blank=True, null=True) 
    github_link3 = models.URLField(max_length=255, blank=True, null=True)
    ppt3_link = models.URLField(max_length=255)

    def __str__(self):
        return f"Round 3 - Team {self.team_no}"




class UniversalSettings(models.Model):
    current_round = models.IntegerField(default=0)
    upload = models.BooleanField(default=False)

    def __str__(self):
        return f"Current Round: {self.current_round}"

class Judge(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    judge_name = models.CharField(max_length=255, default='judge1')  # New field for judge name
    mode = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.judge_name
