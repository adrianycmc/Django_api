from django.contrib import admin

from polls.models import Question, Choice

class CustomAdminSite(admin.AdminSite):
    site_header = "Monty Python administration"


admin_site = CustomAdminSite()
admin_site.register(Question)
admin_site.register(Choice)

