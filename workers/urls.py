from django.urls import path

from .views import workers_tree

app_name = "workers"
urlpatterns = [
    path("", workers_tree),
]
