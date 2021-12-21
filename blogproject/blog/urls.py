from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('published/', views.pub_post_list, name="pub_post_list"),
    path('unpublished/', views.draft_post_list, name="draft_post_list"),
]