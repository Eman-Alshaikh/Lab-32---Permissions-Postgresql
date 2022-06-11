from django.urls import path
from blog.api.viewsets import (
    ArticlesDetailView,
    ArticlesListView 
)


urlpatterns=[
    path('articles-list',ArticlesListView.as_view(),name='atricles_list'),
        path('article-detail/<int:pk>',ArticlesDetailView.as_view(),name='atricle_detail'),

]