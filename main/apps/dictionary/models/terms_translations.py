from auditlog.registry import auditlog
from django.db import models

from main.apps.dictionary.enums import LangChoices
from main.libraries.models import SimpleBaseModel


class TermTranslation(SimpleBaseModel):
    term = models.ForeignKey(
        "dictionary.Term",
        on_delete=models.CASCADE,
        verbose_name="Termín",
        related_name="translations",
    )
    text = models.TextField("Text")
    lang = models.TextField("Jazyk", choices=LangChoices)

    class Meta:
        verbose_name = "Překlad"
        verbose_name_plural = "Překlady"
        ordering = ("created_at",)


auditlog.register(TermTranslation)
