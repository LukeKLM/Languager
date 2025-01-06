from django.contrib import admin

from main.apps.dictionary.admin.term_admin import GroupsInline
from main.apps.dictionary.models import TermGroup


@admin.register(TermGroup)
class TermGroupAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    readonly_fields = ("id",)
    inlines = (GroupsInline,)
