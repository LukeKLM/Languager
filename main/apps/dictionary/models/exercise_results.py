from auditlog.registry import auditlog
from django.db import models

from main.libraries.models import SimpleBaseModel


class ExerciseResult(SimpleBaseModel):
    class ExerciseResult(models.TextChoices):
        CORRECT = "correct", "Correct"
        INCORRECT = "incorrect", "Incorrect"
        UNKNOWN = "unknown", "Unknown"

    term = models.ForeignKey(
        "dictionary.Term",
        on_delete=models.DO_NOTHING,
        verbose_name="Termín",
    )
    result = models.TextField("Výsledek", choices=ExerciseResult)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.DO_NOTHING,
        verbose_name="Uživatel",
    )

    class Meta:
        verbose_name = "Výsledek cvičení"
        verbose_name_plural = "Výsledky cvičení"
        ordering = ("created_at",)


auditlog.register(ExerciseResult)
