from django.views.generic import CreateView

from main.apps.dictionary.forms.terms_form import TermForm
from main.apps.dictionary.models import Term


class TermCreate(CreateView):
    model = Term
    form_class = TermForm
    template_name = "dictionary/terms_create.html"
    success_url = "/"
