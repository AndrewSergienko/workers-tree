from django.shortcuts import render

from . import services


def workers_tree(request):
    director = services.get_root_worker()
    workers = services.get_worker_children(director)
    return render(
        request, "workers/tree.html", {"director": director, "workers": workers}
    )


def worker_children(request, pk):
    worker = services.get_worker_by_id(pk)
    children = services.get_worker_children(worker)
    return render(request, "workers/workers_level.html", {"children": children})
