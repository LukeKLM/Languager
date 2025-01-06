from auditlog.registry import auditlog
from django.db import models

from main.apps.dictionary.enums import LangChoices
from main.libraries.models import SimpleBaseModel


class Term(SimpleBaseModel):
    text = models.TextField("Text")
    lang = models.TextField("Jazyk", choices=LangChoices)
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.DO_NOTHING,
        verbose_name="Vlastník",
    )
    groups = models.ManyToManyField(
        "dictionary.TermGroup",
        verbose_name="Skupiny",
        related_name="terms",
    )

    class Meta:
        verbose_name = "Termín"
        verbose_name_plural = "Termíny"
        ordering = ("created_at",)

    def __str__(self):
        return f"({self.id}) {self.text}"


auditlog.register(Term)
