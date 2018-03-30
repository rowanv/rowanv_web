from django.contrib import admin

from .models import Skill, Project, PastWorkEngagement


class SkillAdmin(admin.ModelAdmin):
	list_display = ('name', )
	search_fields = ('name', )



class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'link', 'code_link', 
    )
    search_fields = ('title', 'description', )


class PastWorkEngagementAdmin(admin.ModelAdmin):
	list_display = ('description', )
	search_fields = ('description', )


admin.site.register(Skill, SkillAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(PastWorkEngagement, PastWorkEngagementAdmin)