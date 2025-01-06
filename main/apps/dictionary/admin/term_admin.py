from django.contrib import admin

from main.apps.dictionary.models import Term


class GroupsInline(admin.TabularInline):
    model = Term.groups.through
    extra = 0


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ("text", "lang", "owner")
    readonly_fields = ("id",)
    inlines = (GroupsInline,)
