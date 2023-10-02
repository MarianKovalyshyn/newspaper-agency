from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from agency.forms import (
    RedactorCreationForm,
    RedactorUsernameSearchForm,
    NewspaperTitleSearchForm,
    TopicNameSearchForm,
    NewspaperForm,
)
from agency.models import Redactor, Newspaper, Topic


def index(request) -> render:
    """View function for the home page of the site."""
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_visits": num_visits + 1,
        "newspaper_list": Newspaper.objects.select_related("topic").prefetch_related("publishers")[:10],
    }
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


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    success_url = reverse_lazy("agency:redactor-list")
    form_class = RedactorCreationForm


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    success_url = reverse_lazy("agency:redactor-list")
    fields = ["first_name", "last_name", "years_of_experience"]


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("agency:redactor-list")


class NewspaperListView(generic.ListView):
    model = Newspaper
    paginate_by = 5
    queryset = Newspaper.objects.select_related("topic")

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
    queryset = Newspaper.objects.select_related("topic")


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    success_url = reverse_lazy("agency:newspaper-list")
    form_class = NewspaperForm


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    success_url = reverse_lazy("agency:newspaper-list")
    form_class = NewspaperForm


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
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
    queryset = Topic.objects.prefetch_related("newspapers")


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    success_url = reverse_lazy("agency:topic-list")
    fields = "__all__"


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    success_url = reverse_lazy("agency:topic-list")
    fields = "__all__"


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("agency:topic-list")
