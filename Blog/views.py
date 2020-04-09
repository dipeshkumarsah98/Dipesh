from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView

)
from .models import Article
# Create your views here.


class articlelistview(ListView):
    template_name = 'article_list.html'
    queryset = Article.objects.all()
