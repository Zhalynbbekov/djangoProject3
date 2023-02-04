from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Zagons)
admin.site.register(Sheeps)
admin.site.register(Deleted_sheeps)

