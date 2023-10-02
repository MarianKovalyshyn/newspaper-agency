from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from agency.forms import (
    RedactorCreationForm,
    RedactorUsernameSearchForm,
    NewspaperTitleSearchForm,
    TopicNameSearchForm,
)
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
    queryset = get_user_model().objects.all()

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(RedactorListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = RedactorUsernameSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self) -> queryset:
        username = self.request.GET.get("username")
        if username:
            return self.queryset.filter(username__icontains=username)
        return self.queryset


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
    queryset = Newspaper.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(NewspaperListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = NewspaperTitleSearchForm(
            initial={"title": title}
        )
        return context

    def get_queryset(self) -> queryset:
        title = self.request.GET.get("title")
        if title:
            return self.queryset.filter(title__icontains=title)
        return self.queryset


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
    queryset = Topic.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(TopicListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TopicNameSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self) -> queryset:
        name = self.request.GET.get("name")
        if name:
            return self.queryset.filter(name__icontains=name)
        return self.queryset

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
