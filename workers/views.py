from django.shortcuts import render


def workers_tree(request):
    return render(request, "workers/tree.html")
