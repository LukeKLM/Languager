from django.db import models


class LangChoices(models.TextChoices):
    CZECH = "cz", "Czech"
    ENGLISH = "en", "English"
