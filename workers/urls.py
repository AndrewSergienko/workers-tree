from django.urls import path

from .views import worker_children, workers_tree

app_name = "workers"
urlpatterns = [
    path("", workers_tree),
    path("<int:pk>/children/", worker_children),
]
