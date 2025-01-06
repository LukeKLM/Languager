from django.contrib import admin

from main.apps.dictionary.models import TermTranslation


@admin.register(TermTranslation)
class TermTranslationAdmin(admin.ModelAdmin):
    list_display = ("id", "term", "text", "lang")
    readonly_fields = ("id",)
