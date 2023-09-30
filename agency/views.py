from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from agency.forms import RedactorCreationForm
from agency.models import Redactor


def index(request) -> render:
    """View function for the home page of the site."""
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {"num_visits": num_visits + 1}
    return render(request, "agency/index.html", context=context)


class RedactorListView(generic.ListView):
    model = Redactor


class RedactorDetailView(generic.DetailView):
    model = Redactor


class RedactorCreateView(generic.CreateView):
    model = Redactor
    success_url = reverse_lazy("agency:redactor-list")
    form_class = RedactorCreationForm


class RedactorUpdateView(generic.UpdateView):
    model = Redactor
    success_url = reverse_lazy("agency:redactor-list")
    fields = ["first_name", "last_name", "years_of_experience"]
