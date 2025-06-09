from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(RubbishType)
admin.site.register(PollutionReport)
admin.site.register(CleanupEvent)