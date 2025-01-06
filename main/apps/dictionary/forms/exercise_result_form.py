from django import forms

from main.apps.dictionary.models import ExerciseResult


class ExerciseResultForm(forms.ModelForm):
    class Meta:
        model = ExerciseResult
        fields = ("term", "result")
