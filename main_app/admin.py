from django.contrib import admin

# Register your models here.
from .models import Card, Team, Fixture

admin.site.register(Card)
admin.site.register(Team)
admin.site.register(Fixture)