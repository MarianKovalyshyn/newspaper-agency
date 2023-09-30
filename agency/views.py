from django.shortcuts import render
from django.views import generic

from agency.models import Redactor


def index(request) -> render:
    """View function for the home page of the site."""
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {"num_visits": num_visits + 1}
    return render(request, "agency/index.html", context=context)


class RedactorListView(generic.ListView):
    model = Redactor
