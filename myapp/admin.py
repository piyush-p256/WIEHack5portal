from django.contrib import admin
from .models import Team, UniversalSettings, Judge, Round1, Round2, Round3

admin.site.register(Team)
admin.site.register(UniversalSettings)
admin.site.register(Judge)  # Register the Judge model
admin.site.register(Round1)  # Register the Judge model
admin.site.register(Round2)  # Register the Judge model
admin.site.register(Round3)  # Register the Judge model

