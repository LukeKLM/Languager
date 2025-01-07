import random

from django.views.generic import ListView

from main.apps.dictionary.models import Term


class ExerciseList(ListView):
    model = Term
    template_name = "dictionary/exercise_list.html"
    success_url = "/"

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(owner=self.request.user)
            .prefetch_related("groups", "translations")
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(object_list=object_list, **kwargs)
        ctx["cards"] = self._get_cards()
        return ctx

    def _get_cards(self):
        cards = [
            {
                "term": term.text,
                "translations": ", ".join(
                    [translation.text for translation in term.translations.all()],
                ),
            }
            for term in self.object_list
        ]
        random.shuffle(cards)
        return cards
