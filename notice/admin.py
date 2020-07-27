from django.contrib import admin
from . models import Notice , Branch , Profile
# Register your models here.

class NoticeAdmin(admin.ModelAdmin):
	list_display=["title","date"]
	list_filter=["date"]
	search_fields=["title","description"]

admin.site.register(Notice,NoticeAdmin)


class BranchAdmin(admin.ModelAdmin):
	list_display=["name"]
	search_fields=["name"]
	

admin.site.register(Branch,BranchAdmin)

admin.site.register(Profile)
