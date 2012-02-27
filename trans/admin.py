from django.contrib import admin
from trans.models import Project, SubProject, Translation, Unit

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'web']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'slug', 'web']

admin.site.register(Project, ProjectAdmin)

class SubProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'project', 'repo', 'branch']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'slug', 'repo', 'branch']

admin.site.register(SubProject, SubProjectAdmin)

class TranslationAdmin(admin.ModelAdmin):
    list_display = ['subproject', 'language', 'translated', 'fuzzy', 'revision', 'filename']
    search_fields = ['subproject__slug', 'language__code', 'translated', 'fuzzy', 'revision', 'filename']

admin.site.register(Translation, TranslationAdmin)

class UnitAdmin(admin.ModelAdmin):
    list_display = ['source', 'target']
    search_fields = ['source', 'target']

admin.site.register(Unit,Unit Admin)

