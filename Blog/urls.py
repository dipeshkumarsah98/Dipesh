from django.urls import path
from .views import (

    articlelistview,

)

app_name = 'articles'

urlpatterns = [
    path('', articlelistview.as_view(), name='article-list'),

]