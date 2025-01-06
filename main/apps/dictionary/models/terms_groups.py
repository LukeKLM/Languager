from auditlog.registry import auditlog
from django.db import models

from main.libraries.models import SimpleBaseModel


class TermGroup(SimpleBaseModel):
    name = models.CharField("Název", max_length=64)

    class Meta:
        verbose_name = "Skupina termínů"
        verbose_name_plural = "Skupiny termínů"
        ordering = ("created_at",)

    def __str__(self):
        return f"({self.id}) {self.name}"


auditlog.register(TermGroup)
