from django.contrib import admin

from .models import Skill, Project


class SkillAdmin(admin.ModelAdmin):
	list_display = ('name', )
	search_fields = ('name', )



class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'link', 'code_link', 
    )
    search_fields = ('title', 'description', )


admin.site.register(Skill, SkillAdmin)
admin.site.register(Project, ProjectAdmin)
