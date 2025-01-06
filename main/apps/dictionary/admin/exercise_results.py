from django.contrib import admin

from main.apps.dictionary.models import ExerciseResult


@admin.register(ExerciseResult)
class ExerciseResultAdmin(admin.ModelAdmin):
    list_display = ("id", "term", "result", "user")
    readonly_fields = ("id",)
