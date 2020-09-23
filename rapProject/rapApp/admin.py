from django.contrib import admin
from .models import Beat, Lyrics, Vote, User
# Register your models here.

admin.site.register(Beat)
admin.site.register(Lyrics)
admin.site.register(Vote)
admin.site.register(User)