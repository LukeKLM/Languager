from django import forms

from main.apps.dictionary.models import TermGroup


class TermGroupForm(forms.ModelForm):
    class Meta:
        model = TermGroup
        fields = ("name",)
