from django.contrib import admin
from team.models import Member

class MemberAdmin(admin.ModelAdmin):
	search_fields = ('name',)

class MemberAdmin(admin.ModelAdmin):
	search_fields = ('name',)

admin.site.register(Member, MemberAdmin)
