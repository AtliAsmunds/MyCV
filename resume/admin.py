from django.contrib import admin
from resume.models import Skill, SuperSkill, Education, Work

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'superskill')
    
@admin.register(SuperSkill)
class SuperSkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'school', 'year_start', 'year_end')

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'work_place', 'year_start', 'year_end')
