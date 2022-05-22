from django.urls import path

from .views import index, group_posts, show_groups

urlpatterns = [
    path("", index, name="index"),
    path("groups", show_groups, name="show_groups"),
    path ("group/<slug:slug>/", group_posts, name="group_posts")
]
