from django.contrib import admin
from .models import Party, Position, Candidate, Vote

# Register your models here.

admin.site.register(Party)
admin.site.register(Position)
admin.site.register(Candidate)
admin.site.register(Vote)
