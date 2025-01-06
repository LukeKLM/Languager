from django.views.generic import CreateView

from main.apps.dictionary.forms.terms_translations_form import TermTranslationForm
from main.apps.dictionary.models import TermTranslation


class TermTranslationCreate(CreateView):
    model = TermTranslation
    form_class = TermTranslationForm
    template_name = "dictionary/terms_translations_create.html"
    success_url = "/"
