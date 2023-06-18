from django.contrib import admin
from .models import Issue, Agent, Mechanic

admin.site.register(Issue)
admin.site.register(Agent)
admin.site.register(Mechanic)

