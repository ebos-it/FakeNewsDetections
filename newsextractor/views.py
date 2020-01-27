from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView
)
from .models import NewsArticle
from .forms import NewsArticleForm

def home(request):
    context = {
        'news_articles': NewsArticle.objects.all(),
        'title': 'Portal - Homepage'
    }
    return render(request,'newsextractor/home.html',context)

class NewsArticlesListView(ListView):
    model = NewsArticle
    template_name = 'newsextractor/home.html'
    context_object_name = 'news_articles'

    ordering = ['-date_posted']

class NewsArticlesCreateView(LoginRequiredMixin, CreateView):
    model = NewsArticle
    form_class = NewsArticleForm

    def form_valid(self, form):
        return super().form_valid(form)

class NewsArticlesDetailView(DetailView):
    model = NewsArticle

class NewsArticlesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = NewsArticle
    success_url = '/'

class NewsArticlesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = NewsArticle
    form_class = NewsArticleForm

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        return True