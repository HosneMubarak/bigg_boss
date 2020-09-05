from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import ChoiceProgram, Article, Comment


@admin.register(Article)
class ArticleAdmin(ImportExportModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'program', 'publish_date', 'ad_published', 'published']
    list_editable = ['publish_date', 'ad_published', 'published']


admin.site.register(ChoiceProgram)
admin.site.register(Comment)
