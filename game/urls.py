from django.urls import path, reverse
from django.http import HttpResponseRedirect

from . import views


app_name = "game"
urlpatterns = [
    path("", lambda *args, **kwargs : HttpResponseRedirect(reverse("game:play"))),
    path("play/", views.play, name="play"),
    # path("leaderboard/", views.index, name="leaderboard"),
]