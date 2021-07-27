from django.conf.urls import url
from django.urls import path

from apps.operations.views import AddFavView, CommentView

urlpatterns = [
    url(r'^lfav/$', AddFavView.as_view(), name="fav"),

    url(r'^comment/$', CommentView.as_view(), name="comment"),
]
