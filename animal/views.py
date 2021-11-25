from dal import autocomplete
from django.db.models import Q
from .models import Animal, Proprietar

class AnimalAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Animal.objects.none()

        qs = Animal.objects.filter()

        if self.q:
            qs = qs.filter(Q(id__icontains=self.q) | Q(microcip__icontains=self.q))

        return qs

class ProprietarAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Proprietar.objects.none()

        qs = Proprietar.objects.filter()

        if self.q:
            qs = qs.filter(id__icontains=self.q)

        return qs
