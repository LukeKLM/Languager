from django import forms

from main.apps.dictionary.models import TermTranslation


class TermTranslationForm(forms.ModelForm):
    class Meta:
        model = TermTranslation
        fields = ("term", "text", "lang")
