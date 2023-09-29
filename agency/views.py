from django.shortcuts import render


def index(request) -> render:
    """View function for the home page of the site."""
    return render(request, "agency/index.html")
