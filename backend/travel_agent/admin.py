from django.contrib import admin

# Register your models here.
from . models import * 
admin.site.register(agent)
admin.site.register(CompanyInfo)
admin.site.register(hotel)
admin.site.register(room)