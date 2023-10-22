from django.views.generic import ListView, DetailView
from PodzialPolski.models import Woj, Pow, Gmi, Miasto

class WojListView(ListView):
    template_name = 'woj.html'
    model = Woj
    context_object_name = 'wojs'


class WojDetailView(DetailView):
    template_name = 'wojdetail.html'
    model = Woj
    context_object_name = 'woj'


class PowDetailView(DetailView):
    template_name = 'powdetail.html'
    model = Pow
    context_object_name = 'pow'

class GmiDetailView(DetailView):
    template_name = 'gmi.html'
    model = Gmi
    context_object_name = 'gmi'


class MiastoDetailView(DetailView):
    template_name = 'miasto.html'
    model = Miasto
    context_object_name = 'miasto'





