from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from agency.forms import RedactorCreationForm
from agency.models import Redactor, Newspaper, Topic


def index(request) -> render:
    """View function for the home page of the site."""
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {"num_visits": num_visits + 1}
    return render(request, "agency/index.html", context=context)


class RedactorListView(generic.ListView):
    model = Redactor
    paginate_by = 5


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


class RedactorDeleteView(generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("agency:redactor-list")


class NewspaperListView(generic.ListView):
    model = Newspaper
    paginate_by = 5


class NewspaperDetailView(generic.DetailView):
    model = Newspaper


class NewspaperCreateView(generic.CreateView):
    model = Newspaper
    success_url = reverse_lazy("agency:newspaper-list")
    fields = "__all__"


class NewspaperUpdateView(generic.UpdateView):
    model = Newspaper
    success_url = reverse_lazy("agency:newspaper-list")
    fields = "__all__"


class NewspaperDeleteView(generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("agency:newspaper-list")


class TopicListView(generic.ListView):
    model = Topic
    paginate_by = 5


class TopicDetailView(generic.DetailView):
    model = Topic


class TopicCreateView(generic.CreateView):
    model = Topic
    success_url = reverse_lazy("agency:topic-list")
    fields = "__all__"


class TopicUpdateView(generic.UpdateView):
    model = Topic
    success_url = reverse_lazy("agency:topic-list")
    fields = "__all__"


class TopicDeleteView(generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("agency:topic-list")
