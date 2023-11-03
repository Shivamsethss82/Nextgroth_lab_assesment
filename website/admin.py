from django.contrib import admin
from .models import Records
# Register your models here.
admin.site.site_header = "Django - CRM App By Shivam Seth"

admin.site.register(Records)