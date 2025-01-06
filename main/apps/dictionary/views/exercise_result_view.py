from django.views.generic import CreateView

from main.apps.dictionary.forms.exercise_result_form import ExerciseResultForm
from main.apps.dictionary.models import ExerciseResult


class TermCreate(CreateView):
    model = ExerciseResult
    form_class = ExerciseResultForm
    template_name = "dictionary/exercise_result_create.html"
    success_url = "/"
