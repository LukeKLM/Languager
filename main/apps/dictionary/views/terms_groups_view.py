from django.views.generic import CreateView

from main.apps.dictionary.forms.terms_groups_form import TermGroupForm
from main.apps.dictionary.models import TermGroup


class TermGroupCreate(CreateView):
    model = TermGroup
    form_class = TermGroupForm
    template_name = "dictionary/terms_groups_create.html"
    success_url = "/"
