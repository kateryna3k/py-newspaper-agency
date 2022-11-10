from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Redactor, Newspaper, Topic


@login_required
def index(request):
    """View function for the home page of the site."""

    num_redactors = Redactor.objects.count()
    num_newspapers = Newspaper.objects.count()
    num_topics = Topic.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_redactors": num_redactors,
        "num_newspapers": num_newspapers,
        "num_topics": num_topics,
        "num_visits": num_visits + 1,
    }

    return render(request, "newspaper/index.html", context=context)


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "newspaper/topic_list.html"
    paginate_by = 5
    queryset = Topic.objects.all()


class RedactorListView(LoginRequiredMixin, generic.ListView):
    pass


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    pass


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    pass


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    pass


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    pass


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    pass


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    pass


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    pass


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    pass


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    pass


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    pass


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    pass


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    pass


class RedactorExperienceUpdateView(LoginRequiredMixin, generic.UpdateView):
    pass


def toggle_assign_to_newspaper(request, pk):
    pass
