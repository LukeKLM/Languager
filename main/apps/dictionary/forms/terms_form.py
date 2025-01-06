from django import forms

from main.apps.dictionary.models import Term


class TermForm(forms.ModelForm):
    class Meta:
        model = Term
        fields = ("text", "lang", "groups")
