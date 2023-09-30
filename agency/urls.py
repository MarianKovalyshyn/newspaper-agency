from django.urls import path

from agency.views import index, RedactorListView, RedactorCreateView

urlpatterns = [
    path("", index, name="index"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("redactors/create", RedactorCreateView.as_view(), name="redactor-create"),
]

app_name = "agency"
