from django.urls import path

from main.apps.dictionary.views import ExerciseList
from main.apps.dictionary.views import TermCreate
from main.apps.dictionary.views import TermGroupCreate
from main.apps.dictionary.views import TermTranslationCreate

urlpatterns = [
    path("terms/", TermCreate.as_view(), name="terms_create"),
    path("terms-groups/", TermGroupCreate.as_view(), name="terms_groups_create"),
    path(
        "terms-translation",
        TermTranslationCreate.as_view(),
        name="terms_translations_create",
    ),
    path("exercise", ExerciseList.as_view(), name="exercise"),
]
