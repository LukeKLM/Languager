from django.views.generic import CreateView

from main.apps.dictionary.forms.terms_form import TermForm
from main.apps.dictionary.models import Term


class TermCreate(CreateView):
    model = Term
    form_class = TermForm
    template_name = "dictionary/terms_create.html"
    success_url = "/"

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.owner = self.request.user

        self.object.save()
        return super().form_valid(form)
