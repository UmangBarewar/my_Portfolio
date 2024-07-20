from django.contrib import admin
from contents.models import *

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ('title', 'description', 'project_category')

admin.site.register(Profile)
admin.site.register(Focus)
admin.site.register(TechnicalSkill)
admin.site.register(ProfessionalSkill)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(ProjectCategory)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ToolsAndTech)
admin.site.register(ProjectImage)
admin.site.register(Recommendation)
admin.site.register(Certification)
admin.site.register(Seminar)
